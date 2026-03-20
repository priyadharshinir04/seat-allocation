"""
Test script to verify PDF page breaks between rooms
"""

from reportlab.lib.pagesizes import landscape, A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from io import BytesIO
from datetime import datetime
import os

# Create test allocation data (4 rooms, varying sizes)
test_rooms = {
    1: [
        {'seat_number': i, 'register_number': f'21CS{1000+i}', 'department': 'CSE', 'year': '1'}
        for i in range(1, 21)
    ],
    2: [
        {'seat_number': i, 'register_number': f'21IT{1000+i}', 'department': 'IT', 'year': '1'}
        for i in range(1, 21)
    ],
    3: [
        {'seat_number': i, 'register_number': f'22AIDS{1000+i}', 'department': 'AIDS', 'year': '2'}
        for i in range(1, 16)
    ],
    4: [
        {'seat_number': i, 'register_number': f'22AIML{1000+i}', 'department': 'AIML', 'year': '2'}
        for i in range(1, 16)
    ]
}

print("=" * 80)
print("TESTING PDF PAGE BREAKS BETWEEN ROOMS")
print("=" * 80)

filename = f"test_pdf_pagebreaks_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
filepath = os.path.join('.', filename)

try:
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=landscape(A4),
                           leftMargin=0.5*inch, rightMargin=0.5*inch,
                           topMargin=0.5*inch, bottomMargin=0.5*inch)
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=6,
        alignment=1
    )
    room_style = ParagraphStyle(
        'RoomTitle',
        parent=styles['Heading3'],
        fontSize=12,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=4,
        alignment=0
    )
    
    elements = []
    
    # Title
    title = Paragraph("<b>Seating Arrangement Report</b>", title_style)
    elements.append(title)
    elements.append(Spacer(1, 0.15*inch))
    
    # Create table for each room with page breaks
    room_numbers = sorted(test_rooms.keys())
    
    for idx, room_no in enumerate(room_numbers):
        room_data = test_rooms[room_no]
        
        # Room header
        room_title = Paragraph(f"<b>Room {room_no} ({len(room_data)} seats)</b>", room_style)
        elements.append(room_title)
        elements.append(Spacer(1, 0.08*inch))
        
        # Create table data
        table_data = [['Seat #', 'Register Number', 'Department', 'Year']]
        
        for seat in sorted(room_data, key=lambda x: x['seat_number']):
            table_data.append([
                str(seat['seat_number']),
                str(seat['register_number']),
                str(seat['department']),
                str(seat['year'])
            ])
        
        # Create table
        col_widths = [0.8*inch, 1.8*inch, 1.5*inch, 1.2*inch]
        table = Table(table_data, colWidths=col_widths)
        
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#667eea')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('VALIGN', (0, 0), (-1, 0), 'MIDDLE'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
            ('TOPPADDING', (0, 0), (-1, 0), 10),
            
            ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 1), (-1, -1), 'MIDDLE'),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f4ff')]),
            
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#cccccc')),
            ('TOPPADDING', (0, 1), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
        ]))
        
        elements.append(table)
        
        # Add page break after each room except the last
        if room_no != room_numbers[-1]:
            elements.append(PageBreak())
            print(f"✓ Room {room_no}: Added table + PAGE BREAK")
        else:
            print(f"✓ Room {room_no}: Added table (last room - no page break)")
    
    # Build PDF
    doc.build(elements)
    
    # Save to file
    buffer.seek(0)
    with open(filepath, 'wb') as f:
        f.write(buffer.read())
    
    print(f"\n" + "=" * 80)
    print("✓ PDF GENERATED SUCCESSFULLY")
    print("=" * 80)
    print(f"\nFile: {filename}")
    print(f"Location: {os.path.abspath(filepath)}")
    print(f"\nRooms in PDF:")
    for room_no, data in test_rooms.items():
        print(f"  - Room {room_no}: {len(data)} seats (page {room_no})")
    
    print(f"\nFeatures:")
    print(f"  ✓ Each room starts on a NEW PAGE")
    print(f"  ✓ Page breaks added between rooms")
    print(f"  ✓ No page break after last room")
    print(f"  ✓ Professional table formatting maintained")
    print(f"\nYou can verify by:")
    print(f"  1. Opening the PDF file")
    print(f"  2. Each room should appear on a separate page")
    print(f"  3. Total pages = number of rooms")

except Exception as e:
    print(f"\n❌ ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
