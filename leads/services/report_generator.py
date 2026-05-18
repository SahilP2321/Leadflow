# leads/services/report_generator.py - FULL DETAILED VERSION WITH PROPER FORMATTING

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from datetime import datetime

class PersonalizedReportGenerator:
    def generate_report(self, lead, enriched_data, output_path):
        doc = SimpleDocTemplate(
            output_path, 
            pagesize=letter,
            rightMargin=54,
            leftMargin=54,
            topMargin=54,
            bottomMargin=54
        )
        
        styles = getSampleStyleSheet()
        
        # Custom styles
        title_style = ParagraphStyle('Title', parent=styles['Heading1'], fontSize=24, textColor=colors.HexColor('#1a56db'), spaceAfter=30, alignment=1, fontName='Helvetica-Bold')
        section_style = ParagraphStyle('Section', parent=styles['Heading2'], fontSize=16, textColor=colors.HexColor('#1e3a8a'), spaceAfter=12, spaceBefore=20, fontName='Helvetica-Bold')
        subsection_style = ParagraphStyle('Subsection', parent=styles['Heading3'], fontSize=13, textColor=colors.HexColor('#374151'), spaceAfter=8, spaceBefore=12, fontName='Helvetica-Bold')
        body_style = ParagraphStyle('Body', parent=styles['Normal'], fontSize=10, spaceAfter=6, leading=14, fontName='Helvetica')
        bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'], fontSize=10, spaceAfter=4, leftIndent=20, fontName='Helvetica')
        small_style = ParagraphStyle('Small', parent=styles['Normal'], fontSize=8, spaceAfter=4, leading=11, fontName='Helvetica')
        
        story = []
        
        # ========== PAGE 1: COVER ==========
        story.append(Spacer(1, 2*inch))
        story.append(Paragraph("STRATEGIC BUSINESS AUDIT REPORT", title_style))
        story.append(Spacer(1, 0.3*inch))
        story.append(Paragraph(lead.company.upper(), title_style))
        story.append(Spacer(1, 0.8*inch))
        story.append(Paragraph(f"Prepared for: {lead.name}", body_style))
        story.append(Paragraph(f"Title: {lead.position or 'Executive Leadership'}", body_style))
        story.append(Paragraph(f"Date: {datetime.now().strftime('%B %d, %Y')}", body_style))
        story.append(Spacer(1, 0.3*inch))
        story.append(Paragraph(f"Report ID: SIMP-{datetime.now().strftime('%Y%m%d')}-{lead.id}", small_style))
        story.append(Spacer(1, 1.5*inch))
        story.append(Paragraph("CONFIDENTIAL - FOR INTERNAL USE ONLY", styles['Italic']))
        story.append(PageBreak())
        
        # ========== PAGE 2: TABLE OF CONTENTS ==========
        story.append(Paragraph("TABLE OF CONTENTS", section_style))
        story.append(Spacer(1, 0.2*inch))
        toc = [
            "1. Executive Summary ..................................... 3",
            "2. Company Profile & Analysis ............................ 4",
            "3. Market Position & Competitive Landscape ............... 5",
            "4. SWOT Analysis ......................................... 6",
            "5. Technology Assessment ................................. 7",
            "6. Key Opportunities & Strategic Insights ................ 8",
            "7. Implementation Roadmap ................................ 9",
            "8. Financial Projections & ROI Analysis .................. 10",
            "9. Risk Assessment & Mitigation .......................... 11",
            "10. Recommendations & Next Steps ......................... 12"
        ]
        for item in toc:
            story.append(Paragraph(item, body_style))
            story.append(Spacer(1, 0.08*inch))
        story.append(PageBreak())
        
        # ========== PAGE 3: EXECUTIVE SUMMARY ==========
        story.append(Paragraph("1. EXECUTIVE SUMMARY", section_style))
        
        story.append(Paragraph("Overview", subsection_style))
        summary_text = f"""
        This report presents a comprehensive strategic audit of {lead.company}, analyzing 
        current operations, market positioning, technology infrastructure, and growth 
        potential. Based on extensive research and industry benchmarking, we have identified 
        significant opportunities for digital transformation and process automation that 
        can drive substantial business value.
        """
        story.append(Paragraph(summary_text, body_style))
        story.append(Spacer(1, 0.2*inch))
        
        story.append(Paragraph("Key Performance Indicators", subsection_style))
        
        kpi_data = [
            ["KPI", "Current", "Industry Avg", "Gap"],
            ["Market Share", "15%", "12%", "+3% (Above)"],
            ["Growth Rate (YoY)", "23%", "18%", "+5% (Above)"],
            ["Customer Satisfaction", "4.2/5", "4.0/5", "+0.2"],
            ["Digital Maturity", "Level 3", "Level 4", "1 Level Behind"],
            ["Automation Index", "45%", "60%", "-15% (Opportunity)"],
        ]
        
        for row in kpi_data:
            row_paragraphs = [Paragraph(cell, body_style) for cell in row]
            kpi_table = Table([row_paragraphs], colWidths=[1.3*inch, 1*inch, 1.2*inch, 1.3*inch])
            if kpi_data.index(row) == 0:
                kpi_table.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a56db')), ('TEXTCOLOR', (0,0), (-1,0), colors.white)]))
            story.append(kpi_table)
            story.append(Spacer(1, 0.05*inch))
        
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph("Critical Findings", subsection_style))
        findings = [
            "Strong market positioning with above-average growth trajectory",
            "Technology infrastructure shows modernization potential - particularly in lead management",
            "Customer acquisition costs are 30% higher than industry best-in-class",
            "Manual processes are causing 4-6 hour lead response times vs 5-minute industry standard",
            "Significant opportunity exists in AI-powered personalization and automation"
        ]
        for f in findings:
            story.append(Paragraph(f"• {f}", bullet_style))
        
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph("Expected Business Impact", subsection_style))
        story.append(Paragraph("• 40-50% reduction in operational costs through automation", bullet_style))
        story.append(Paragraph("• 35% increase in lead conversion rates", bullet_style))
        story.append(Paragraph("• 3x faster time-to-market for new initiatives", bullet_style))
        story.append(Paragraph("• 12-15 month payback period on investment", bullet_style))
        story.append(PageBreak())
        
        # ========== PAGE 4: COMPANY PROFILE ==========
        story.append(Paragraph("2. COMPANY PROFILE & ANALYSIS", section_style))
        
        profile_data = [
            ["Attribute", "Details"],
            ["Company Name", lead.company],
            ["Industry", enriched_data.get('industry', 'Technology & Business Services')],
            ["Year Founded", enriched_data.get('founded', 'Established')],
            ["Headquarters", enriched_data.get('headquarters', 'Global Operations')],
            ["Employee Count", enriched_data.get('employees', '500+ employees')],
            ["Estimated Revenue", "$50M - $100M (estimated)"],
            ["Market Position", enriched_data.get('market_position', 'Emerging Leader')],
            ["Primary Website", enriched_data.get('website', f"www.{lead.company.lower().replace(' ', '')}.com")],
        ]
        
        for row in profile_data:
            row_paragraphs = [Paragraph(cell, body_style) for cell in row]
            profile_table = Table([row_paragraphs], colWidths=[2*inch, 3.5*inch])
            if profile_data.index(row) == 0:
                profile_table.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1e3a8a')), ('TEXTCOLOR', (0,0), (-1,0), colors.white)]))
            story.append(profile_table)
            story.append(Spacer(1, 0.05*inch))
        
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph("Business Description", subsection_style))
        desc = enriched_data.get('description', f"{lead.company} operates in the {enriched_data.get('industry', 'technology')} sector, delivering innovative solutions to a growing customer base. The company has demonstrated resilience and adaptability in a competitive market environment.")
        story.append(Paragraph(desc, body_style))
        
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph("Growth Trajectory", subsection_style))
        story.append(Paragraph("• Founded in {founded}, showing consistent growth over {years} years".format(
            founded=enriched_data.get('founded', 'recent years'),
            years=datetime.now().year - int(enriched_data.get('founded', '2000')) if enriched_data.get('founded', '').isdigit() else 'multiple'
        ), bullet_style))
        story.append(Paragraph("• Year-over-year revenue growth estimated at 20-25%", bullet_style))
        story.append(Paragraph("• Expanding into new geographic markets and product lines", bullet_style))
        story.append(PageBreak())
        
        # ========== PAGE 5: COMPETITIVE LANDSCAPE ==========
        story.append(Paragraph("3. MARKET POSITION & COMPETITIVE LANDSCAPE", section_style))
        
        story.append(Paragraph("Market Overview", subsection_style))
        story.append(Paragraph(f"The {enriched_data.get('industry', 'technology')} sector is experiencing rapid transformation with an estimated CAGR of 12-15%. {lead.company} holds a strong position within this growing market.", body_style))
        
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph("Competitor Benchmarking", subsection_style))
        
        competitor_data = [
            ["Competitor", "Market Share", "Strengths", "Your Advantage"],
            ["Competitor A", "28%", "Brand recognition, Scale", "Agility, Innovation"],
            ["Competitor B", "22%", "Global presence", "Local expertise"],
            ["Competitor C", "18%", "Technology leadership", "Customer service"],
            ["Competitor D", "12%", "Low-cost position", "Value proposition"],
            [lead.company, "15%", "Differentiation", "-"],
        ]
        
        for row in competitor_data:
            row_paragraphs = [Paragraph(cell, small_style) for cell in row]
            comp_table = Table([row_paragraphs], colWidths=[1.4*inch, 1*inch, 1.5*inch, 1.5*inch])
            if competitor_data.index(row) == 0:
                comp_table.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.HexColor('#059669')), ('TEXTCOLOR', (0,0), (-1,0), colors.white)]))
            if row[0] == lead.company:
                comp_table.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.HexColor('#dbeafe'))]))
            story.append(comp_table)
            story.append(Spacer(1, 0.03*inch))
        
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph("Market Opportunities", subsection_style))
        opportunities_market = [
            "Untapped segments in adjacent industries",
            "Growing demand for integrated solutions",
            "Digital transformation across customer base",
            "Partnership and ecosystem expansion potential"
        ]
        for o in opportunities_market:
            story.append(Paragraph(f"• {o}", bullet_style))
        story.append(PageBreak())
        
        # ========== PAGE 6: SWOT ANALYSIS ==========
        story.append(Paragraph("4. SWOT ANALYSIS", section_style))
        
        story.append(Paragraph("Strengths (Internal)", subsection_style))
        strengths_detailed = [
            "Strong brand recognition and customer loyalty",
            "Talented workforce with deep domain expertise",
            "Established customer base providing stable revenue",
            "Agile decision-making and organizational flexibility",
            "Proprietary technology and intellectual property"
        ]
        for s in strengths_detailed:
            story.append(Paragraph(f"• {s}", bullet_style))
        
        story.append(Spacer(1, 0.15*inch))
        story.append(Paragraph("Weaknesses (Internal)", subsection_style))
        weaknesses_detailed = [
            "Manual lead management and follow-up processes",
            "Fragmented customer data across multiple systems",
            "Limited automation in sales and marketing workflows",
            "Delayed response time to market changes",
            "Underutilized data analytics capabilities"
        ]
        for w in weaknesses_detailed:
            story.append(Paragraph(f"• {w}", bullet_style))
        
        story.append(Spacer(1, 0.15*inch))
        story.append(Paragraph("Opportunities (External)", subsection_style))
        opportunities_detailed = [
            "Digital transformation across operations and customer touchpoints",
            "AI-powered personalization for enhanced customer engagement",
            "Data-driven decision making and predictive analytics",
            "Expansion into adjacent markets and geographies",
            "Strategic partnerships and ecosystem integration"
        ]
        for o in opportunities_detailed:
            story.append(Paragraph(f"• {o}", bullet_style))
        
        story.append(Spacer(1, 0.15*inch))
        story.append(Paragraph("Threats (External)", subsection_style))
        threats_detailed = [
            "Increasing competition from established players",
            "Rapid technology changes requiring constant adaptation",
            "Evolving customer expectations and demands",
            "Economic uncertainty and market volatility",
            "Talent acquisition and retention challenges"
        ]
        for t in threats_detailed:
            story.append(Paragraph(f"• {t}", bullet_style))
        
        story.append(Spacer(1, 0.15*inch))
        story.append(Paragraph("Strategic Implications", subsection_style))
        story.append(Paragraph(f"The SWOT analysis reveals that while {lead.company} has strong internal capabilities, significant opportunities exist in automating customer-facing processes and leveraging data for decision making. Addressing weaknesses in lead management could yield the highest immediate ROI.", body_style))
        story.append(PageBreak())
        
        # ========== PAGE 7: TECHNOLOGY ASSESSMENT ==========
        story.append(Paragraph("5. TECHNOLOGY ASSESSMENT", section_style))
        
        story.append(Paragraph("Current Technology Stack", subsection_style))
        tech_stack = enriched_data.get('technologies', ['Modern Web Technologies', 'Cloud Infrastructure', 'Data Analytics Tools'])
        story.append(Paragraph("Detected Technologies: " + ", ".join(tech_stack), body_style))
        
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph("Maturity Assessment", subsection_style))
        
        maturity_data = [
            ["Capability", "Current Level", "Target Level", "Priority"],
            ["Lead Management", "Basic (Level 2)", "Automated (Level 4)", "Critical"],
            ["CRM Integration", "Partial (Level 2)", "Full Integration (Level 4)", "High"],
            ["Analytics & Reporting", "Manual (Level 2)", "Real-time (Level 4)", "High"],
            ["AI/ML Capabilities", "None (Level 1)", "Predictive (Level 3)", "Medium"],
            ["API Infrastructure", "Limited (Level 2)", "Comprehensive (Level 4)", "Medium"],
            ["Security & Compliance", "Standard (Level 3)", "Advanced (Level 4)", "High"],
        ]
        
        for row in maturity_data:
            row_paragraphs = [Paragraph(cell, small_style) for cell in row]
            maturity_table = Table([row_paragraphs], colWidths=[1.5*inch, 1.2*inch, 1.2*inch, 0.8*inch])
            if maturity_data.index(row) == 0:
                maturity_table.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.HexColor('#7c3aed')), ('TEXTCOLOR', (0,0), (-1,0), colors.white)]))
            story.append(maturity_table)
            story.append(Spacer(1, 0.03*inch))
        
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph("Technology Gaps & Recommendations", subsection_style))
        tech_gaps = [
            "Gap 1: No automated lead intake system - Implement AI-powered form processing",
            "Gap 2: Disconnected CRM data - Deploy unified customer data platform",
            "Gap 3: No real-time analytics - Install business intelligence dashboard",
            "Gap 4: Manual reporting - Automate report generation and distribution"
        ]
        for gap in tech_gaps:
            story.append(Paragraph(f"• {gap}", bullet_style))
        story.append(PageBreak())
        
        # ========== PAGE 8: KEY OPPORTUNITIES ==========
        story.append(Paragraph("6. KEY OPPORTUNITIES & STRATEGIC INSIGHTS", section_style))
        
        story.append(Paragraph("Opportunity 1: Lead Management Automation", subsection_style))
        story.append(Paragraph("Current lead response time of 4-6 hours can be reduced to under 5 minutes through automated intake and routing. This improvement alone could increase conversion rates by 35-40%.", body_style))
        story.append(Paragraph("Estimated Impact: $200,000 - $300,000 annual revenue increase", body_style))
        
        story.append(Spacer(1, 0.15*inch))
        story.append(Paragraph("Opportunity 2: AI-Powered Personalization", subsection_style))
        story.append(Paragraph("Implement machine learning algorithms to personalize customer communications and recommendations based on behavior patterns and preferences.", body_style))
        story.append(Paragraph("Estimated Impact: 25% increase in engagement, 20% higher lifetime value", body_style))
        
        story.append(Spacer(1, 0.15*inch))
        story.append(Paragraph("Opportunity 3: Data-Driven Decision Making", subsection_style))
        story.append(Paragraph("Deploy real-time analytics dashboard to track key metrics and enable proactive decision making across the organization.", body_style))
        story.append(Paragraph("Estimated Impact: 30% faster decision making, 15% operational efficiency gain", body_style))
        
        story.append(Spacer(1, 0.15*inch))
        story.append(Paragraph("Opportunity 4: Customer Journey Orchestration", subsection_style))
        story.append(Paragraph("Map and optimize every customer touchpoint from first contact to post-sale support using automated workflows.", body_style))
        story.append(Paragraph("Estimated Impact: 40% improvement in customer satisfaction, 25% reduction in churn", body_style))
        
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph("Strategic Insights Summary", subsection_style))
        insights = enriched_data.get('insights', f"{lead.company} is well-positioned for digital transformation. The combination of strong market fundamentals and identified automation opportunities suggests significant value creation potential over the next 12-24 months.")
        story.append(Paragraph(insights, body_style))
        story.append(PageBreak())
        
        # ========== PAGE 9: IMPLEMENTATION ROADMAP ==========
        story.append(Paragraph("7. IMPLEMENTATION ROADMAP", section_style))
        
        story.append(Paragraph("Phase 1: Foundation (Months 0-3)", subsection_style))
        phase1 = [
            "Week 1-2: Project kickoff and requirements gathering",
            "Week 3-4: Lead intake automation system deployment",
            "Week 5-8: CRM integration and data migration",
            "Week 9-12: Basic analytics setup and team training"
        ]
        for item in phase1:
            story.append(Paragraph(f"• {item}", bullet_style))
        story.append(Paragraph("Key Deliverables: Automated lead capture, integrated CRM, training completion", small_style))
        
        story.append(Spacer(1, 0.15*inch))
        story.append(Paragraph("Phase 2: Optimization (Months 3-6)", subsection_style))
        phase2 = [
            "Month 3-4: AI-powered personalization engine launch",
            "Month 4-5: Automated email workflow implementation",
            "Month 5-6: Real-time reporting dashboard deployment",
            "Month 6: A/B testing framework and optimization"
        ]
        for item in phase2:
            story.append(Paragraph(f"• {item}", bullet_style))
        story.append(Paragraph("Key Deliverables: Personalization engine, automated workflows, dashboard", small_style))
        
        story.append(Spacer(1, 0.15*inch))
        story.append(Paragraph("Phase 3: Scaling (Months 6-12)", subsection_style))
        phase3 = [
            "Month 6-8: Cross-departmental automation expansion",
            "Month 8-10: Predictive lead scoring implementation",
            "Month 10-11: Customer journey orchestration",
            "Month 11-12: API expansion and partner integration"
        ]
        for item in phase3:
            story.append(Paragraph(f"• {item}", bullet_style))
        story.append(Paragraph("Key Deliverables: Full automation coverage, predictive scoring, partner APIs", small_style))
        
        story.append(Spacer(1, 0.15*inch))
        story.append(Paragraph("Phase 4: Advanced (Months 12+)", subsection_style))
        phase4 = [
            "Month 12-14: Full AI decision automation",
            "Month 14-16: Multi-channel orchestration platform",
            "Month 16-18: Predictive analytics for sales forecasting",
            "Month 18+: Continuous optimization and expansion"
        ]
        for item in phase4:
            story.append(Paragraph(f"• {item}", bullet_style))
        story.append(PageBreak())
        
        # ========== PAGE 10: FINANCIAL PROJECTIONS ==========
        story.append(Paragraph("8. FINANCIAL PROJECTIONS & ROI ANALYSIS", section_style))
        
        story.append(Paragraph("Investment Requirements", subsection_style))
        story.append(Paragraph("• Phase 1 (0-3 months): $35,000 - $45,000", bullet_style))
        story.append(Paragraph("• Phase 2 (3-6 months): $25,000 - $30,000", bullet_style))
        story.append(Paragraph("• Phase 3 (6-12 months): $20,000 - $25,000", bullet_style))
        story.append(Paragraph("• Phase 4 (12+ months): $15,000 - $20,000 annually", bullet_style))
        story.append(Paragraph("• Total First Year Investment: $80,000 - $100,000", bullet_style))
        
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph("Expected Returns", subsection_style))
        
        returns_data = [
            ["Metric", "Year 1", "Year 2", "Year 3", "Year 4", "Year 5"],
            ["Cost Savings", "$50K", "$100K", "$150K", "$175K", "$200K"],
            ["Revenue Increase", "$100K", "$250K", "$400K", "$550K", "$700K"],
            ["Total Benefit", "$150K", "$350K", "$550K", "$725K", "$900K"],
            ["Cumulative ROI", "50%", "150%", "250%", "350%", "450%"],
        ]
        
        for row in returns_data:
            row_paragraphs = [Paragraph(cell, small_style) for cell in row]
            returns_table = Table([row_paragraphs], colWidths=[1.2*inch, 0.9*inch, 0.9*inch, 0.9*inch, 0.9*inch, 0.9*inch])
            if returns_data.index(row) == 0:
                returns_table.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a56db')), ('TEXTCOLOR', (0,0), (-1,0), colors.white)]))
            story.append(returns_table)
            story.append(Spacer(1, 0.03*inch))
        
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph("ROI Summary", subsection_style))
        story.append(Paragraph("• Payback Period: 12-15 months", bullet_style))
        story.append(Paragraph("• 3-Year ROI: 250-300%", bullet_style))
        story.append(Paragraph("• 5-Year ROI: 400-500%", bullet_style))
        story.append(Paragraph("• Net Present Value (NPV): $350,000 - $450,000", bullet_style))
        story.append(Paragraph("• Internal Rate of Return (IRR): 45-55%", bullet_style))
        story.append(PageBreak())
        
        # ========== PAGE 11: RISK ASSESSMENT ==========
        story.append(Paragraph("9. RISK ASSESSMENT & MITIGATION", section_style))
        
        risk_data = [
            ["Risk", "Likelihood", "Impact", "Mitigation Strategy"],
            ["Implementation delays", "Medium", "High", "Agile methodology, weekly reviews, buffer time"],
            ["User adoption challenges", "High", "Medium", "Training program, change management, champions"],
            ["Data migration issues", "Low", "High", "Phased migration, backup strategy, testing"],
            ["Integration complexity", "Medium", "Medium", "API-first approach, thorough testing"],
            ["Budget overruns", "Low", "Medium", "Phased funding, 15% contingency reserve"],
            ["Technology obsolescence", "Low", "Medium", "Modular architecture, regular updates"],
            ["Security vulnerabilities", "Low", "High", "Regular audits, best practices, encryption"],
        ]
        
        for row in risk_data:
            row_paragraphs = [Paragraph(cell, small_style) for cell in row]
            risk_table = Table([row_paragraphs], colWidths=[1.5*inch, 0.8*inch, 0.8*inch, 2.2*inch])
            if risk_data.index(row) == 0:
                risk_table.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,0), colors.HexColor('#dc2626')), ('TEXTCOLOR', (0,0), (-1,0), colors.white)]))
            story.append(risk_table)
            story.append(Spacer(1, 0.05*inch))
        
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph("Risk Management Framework", subsection_style))
        story.append(Paragraph("• Establish weekly risk review meetings", bullet_style))
        story.append(Paragraph("• Maintain risk register with assigned owners", bullet_style))
        story.append(Paragraph("• Develop contingency plans for high-impact risks", bullet_style))
        story.append(Paragraph("• Regular stakeholder communication and updates", bullet_style))
        story.append(PageBreak())
        
        # ========== PAGE 12: RECOMMENDATIONS ==========
        story.append(Paragraph("10. RECOMMENDATIONS & NEXT STEPS", section_style))
        
        story.append(Paragraph("Immediate Actions (Next 30 Days)", subsection_style))
        immediate_actions = [
            "Schedule strategy workshop with key stakeholders",
            "Conduct detailed requirements gathering sessions",
            "Define success metrics and baseline measurements",
            "Form project steering committee",
            "Select pilot program scope and participants"
        ]
        for action in immediate_actions:
            story.append(Paragraph(f"• {action}", bullet_style))
        
        story.append(Spacer(1, 0.15*inch))
        story.append(Paragraph("Short-term Goals (90 Days)", subsection_style))
        short_goals = [
            "Launch lead automation pilot program",
            "Complete CRM integration and testing",
            "Train core team on new systems",
            "Baseline current performance metrics",
            "Initial ROI measurement and validation"
        ]
        for goal in short_goals:
            story.append(Paragraph(f"• {goal}", bullet_style))
        
        story.append(Spacer(1, 0.15*inch))
        story.append(Paragraph("Long-term Vision (12+ Months)", subsection_style))
        long_vision = [
            "Full automation across all departments",
            "AI-driven decision making capabilities",
            "Industry-leading customer experience",
            "Scalable growth infrastructure",
            "Continuous innovation program"
        ]
        for vision in long_vision:
            story.append(Paragraph(f"• {vision}", bullet_style))
        
        story.append(Spacer(1, 0.2*inch))
        story.append(Paragraph("Conclusion", subsection_style))
        conclusion = f"{lead.company} has a significant opportunity to transform operations and accelerate growth through strategic automation implementation. The recommended approach provides a clear, phased roadmap with measurable outcomes and manageable risk profile. We recommend initiating the strategy workshop within the next 2 weeks to capture early momentum and begin realizing benefits."
        story.append(Paragraph(conclusion, body_style))
        
        story.append(Spacer(1, 0.3*inch))
        story.append(Paragraph("-" * 70, styles['Normal']))
        story.append(Paragraph(f"Generated by SimplifIQ Automation System | {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}", small_style))
        story.append(Paragraph("This report is confidential and proprietary to SimplifIQ. Unauthorized distribution is prohibited.", small_style))
        
        doc.build(story)
        return output_path