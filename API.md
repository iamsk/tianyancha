#### 企业基本信息


* method:  ic_baseinfo
* name 企业基本信息
* desc 可以通过公司名称或ID获取企业基本信息，企业基本信息包括公司名称或ID、类型、成立日期、经营状态、注册资本、法人、工商注册号、统一社会信用代码、组织机构代码、纳税人识别号等字段信息
* path ic/baseinfo/2.0
* params ['id', 'name', 'keyword']


#### 企业基本信息（含企业联系方式）


* method:  ic_baseinfoV2
* name 企业基本信息（含企业联系方式）
* desc 可以通过公司名称或ID或ID称获取企业基本信息和企业联系方式，包括公司名称或ID、类型、成立日期、电话、邮箱、网址等字段的详细信息
* path ic/baseinfoV2/2.0
* params ['id', 'name', 'keyword']


#### 企业基本信息（含主要人员）


* method:  ic_baseinfoV3
* name 企业基本信息（含主要人员）
* desc 可以通过公司名称或ID获取企业基本信息和主要人员信息，包括公司名称或ID、类型、成立日期、联系方式、主要人员名称、职位等字段的详细信息
* path ic/baseinfoV3/2.0
* params ['id', 'name', 'keyword']


#### 特殊企业基本信息


* method:  _services_v4_open_xgbaseinfoV2
* name 特殊企业基本信息
* desc 可以通过公司名称或ID获取特殊企业基本信息，包含香港公司、社会组织、律所、事业单位、基金会这些特殊企业，不同社会团体所呈现的信息维度不同
* path /services/v4/open/xgbaseinfoV2
* params ['id', 'name', 'keyword']


#### 企业三要素验证


* method:  ic_verify
* name 企业三要素验证
* desc 可以通过输入企业名称、法人、注册号 /组织机构代码 /统一社会信用代码，验证三者是否匹配一致
* path ic/verify
* params ['name', 'code', 'legalPersonName']


#### 工商快照


* method:  ic_snapshot
* name 工商快照
* desc 可以通过公司名称或ID获取工商快照信息，工商快照信息包括工商官网信息快照、营业执照信息、股东及出资信息等
* path ic/snapshot
* params ['name', 'id', 'keyword']


#### 企业类型


* method:  ic_companyType
* name 企业类型
* desc 可以通过公司名称或ID获取企业类型信息
* path ic/companyType
* params ['name', 'id', 'keyword']


#### 企业联系方式


* method:  ic_contact
* name 企业联系方式
* desc 可以通过公司名称或ID获取企业联系方式信息，企业联系方式信息包括邮箱、网址、电话等字段的详细信息
* path ic/contact
* params ['name', 'id', 'keyword']


#### 主要人员


* method:  ic_staff
* name 主要人员
* desc 可以通过公司名称或ID获取企业主要人员信息，主要人员信息包括董事、监事、高级管理人员姓名、职位、主要人员总数等字段的详细信息
* path ic/staff/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 历史主要人员


* method:  hi_members
* name 历史主要人员
* desc 可以通过公司名称或ID获取历史主要人员信息，历史主要人员信息包括法人名、变更时间、主要人员名、变更时间、股东名、退股时间等字段的信息
* path hi/members
* params ['id', 'name', 'keyword']


#### 企业股东


* method:  ic_holder
* name 企业股东
* desc 可以通过公司名称或ID获取企业股东信息，股东信息包括股东名、出资比例、出资金额、股东总数等字段的详细信息
* path ic/holder/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 历史股东信息


* method:  hi_holder
* name 历史股东信息
* desc 可以通过公司名称或ID获取企业历史的股东信息，历史股东信息包括股东名、出资比例、认缴金额、股东总数等字段信息
* path hi/holder/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 公司公示-股东出资


* method:  ic_holderList
* name 公司公示-股东出资
* desc 可以通过公司名称或ID获取股东及出自信息，股东及出资信息包括股东名、出资比例、出资金额、股东总数等字段的详细信息
* path ic/holderList/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 公司公示-股权变更


* method:  ic_holderChange
* name 公司公示-股权变更
* desc 可以通过公司名称或ID获取企业股权变更信息，股权变更包括变更前后的股东名、变更时间等字段的详细信息
* path ic/holderChange/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 对外投资


* method:  ic_inverst
* name 对外投资
* desc 可以通过公司名称或ID获取企业对外投资信息，对外投资信息包括被投资企业、企业法人、投资占比、对外投资总数等字段的详细信息
* path ic/inverst/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 历史对外投资


* method:  hi_invest
* name 历史对外投资
* desc 历史对外投资
* path hi/invest/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 分支机构


* method:  ic_branch
* name 分支机构
* desc 可以通过公司名称或ID获取企业分支机构信息，分支机构信息包括分公司名称或ID、企业法人、经营状态、分公司总数等字段的详细信息
* path ic/branch/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 总公司


* method:  ic_parentCompany
* name 总公司
* desc 可以通过公司名称或ID获取企业总公司信息，总公司信息包括总公司名称或ID、企业法人、经营状态、注册资本等字段的详细信息
* path ic/parentCompany/2.0
* params ['id', 'name', 'keyword']


#### 企业年报


* method:  ic_annualreport
* name 企业年报
* desc 可以通过公司名称或ID获取企业年报，企业年报包括企业基本信息、股东及出资信息、企业资产状况信息、对外投资信息等字段的详细信息
* path ic/annualreport/2.0
* params ['id', 'name', 'keyword']


#### 变更记录


* method:  ic_changeinfo
* name 变更记录
* desc 可以通过公司名称或ID获取企业变更记录，变更记录包括工商变更事项、变更前后信息等字段的详细信息
* path ic/changeinfo/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 历史工商信息


* method:  hi_ic
* name 历史工商信息
* desc 历史工商信息
* path hi/ic/2.0
* params ['id', 'name', 'keyword']


#### 司法解析


* method:  jr_judicialCase
* name 司法解析
* desc 可以通过公司名称或ID获取司法解析信息，司法解析信息包括案件名称、案件类型、案件身份、案由、相关案号、最新审理程序、最新审理日期等字段的详细信息
* path jr/judicialCase/2.0
* params ['id', 'name', 'pageNum', 'pageSize', 'keyword']


#### 法律诉讼


* method:  jr_lawSuit
* name 法律诉讼
* desc 可以通过公司名称或ID获取企业法律诉讼信息，法律诉讼包括案件名称、案由、案件身份、案号等字段的详细信息
* path jr/lawSuit/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 历史法律诉讼


* method:  hi_lawsuit
* name 历史法律诉讼
* desc 可以通过公司名称或ID获取企业历史的法律诉讼信息，历史法律诉讼包括案件名称、案由、案件身份、案号等字段信息
* path hi/lawsuit/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 开庭公告


* method:  jr_ktannouncement
* name 开庭公告
* desc 可以通过公司名称或ID获取企业开庭公告，开庭公告信息包括被告/被上诉人、法院、原告/上诉人、开庭日期、案由、内部ID、案号等字段的详细信息
* path jr/ktannouncement/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 历史开庭公告


* method:  hi_announcement
* name 历史开庭公告
* desc 可以通过公司名称或ID获取企业历史的开庭公告，历史开庭公告信息包括被告/被上诉人、法院、原告/上诉人、开庭日期、案由、内部ID、案号等字段信息
* path hi/announcement/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 法院公告


* method:  jr_courtAnnouncement
* name 法院公告
* desc 可以通过公司名称或ID获取企业法院公告，法院公告信息包括执行法院、案件内容、公告类型、刊登日期、公司名、当事人等字段的详细信息
* path jr/courtAnnouncement/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 历史法院公告


* method:  hi_court
* name 历史法院公告
* desc 可以通过公司名称或ID获取企业历史的法院公告，历史法院公告信息包括执行法院、案件内容、公告类型、刊登日期、公司名、当事人等字段信息
* path hi/court/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 送达公告


* method:  jr_sendAnnouncement
* name 送达公告
* desc 可以通过公司名称或ID获取送达公告信息，送达公告信息包括公告名称、法院名称、公告内容、发布日期等字段的详细信息
* path jr/sendAnnouncement/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 立案信息


* method:  jr_courtRegister
* name 立案信息
* desc 可以通过公司名称或ID获取立案信息，立案信息包括案件编号、案由、立案时间、案件原被告双方信息等字段的详细信息
* path jr/courtRegister/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 司法协助


* method:  _services_v4_open_judicial
* name 司法协助
* desc 可以通过公司名称或ID获取司法协助信息，司法协助信息包括执行法院、案件内容、被执行人名称等字段的详细信息
* path /services/v4/open/judicial
* params ['name', 'id', 'keyword', 'pageNum', 'pageSize']


#### 司法协助详情


* method:  _services_v4_open_getJudicialDetail
* name 司法协助详情
* desc 根据司法协助ID获取司法协助详情，判断司法协助类型，包括股权变更、股权冻结、结解除冻结、司法协助续行、股权数额、司法冻结失效及对应的详细信息
* path /services/v4/open/getJudicialDetail
* params ['assistanceId']


#### 历史司法协助


* method:  hi_judicial
* name 历史司法协助
* desc 可以通过公司名称或ID获取企业历史的司法协助信息，历史司法协助信息包括执行法院、案件内容、被执行人名称等字段信息
* path hi/judicial/2.0
* params ['name', 'id', 'keyword', 'pageNum', 'pageSize']


#### 历史司法协助详情


* method:  hi_judicial_detail
* name 历史司法协助详情
* desc 根据司法协助ID获取历史的司法协助详情，判断司法协助类型，历史司法协助详情包括股权变更、股权冻结、结解除冻结、司法协助续行、股权数额、司法冻结失效及对应的详细信息
* path hi/judicial/detail/2.0
* params ['businessId']


#### 破产重整


* method:  jr_bankruptcy
* name 破产重整
* desc 可以通过公司名称或ID获取破产重整信息，破产重整信息包括破产案件公开时间、申请人、被申请人、申请对象等字段的详细信息
* path jr/bankruptcy/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 破产重整详情


* method:  jr_bankruptcy_detail
* name 破产重整详情
* desc 可以通过公司名称或ID获取破产重整信息，破产重整信息包括破产案件公开时间、申请人、被申请人、申请对象、管理人主要负责人等字段的详细信息
* path jr/bankruptcy/detail/2.0
* params ['gid', 'uuid']


#### 被执行人


* method:  jr_zhixinginfo
* name 被执行人
* desc 可以通过公司名称或ID获取被执行人信息，被执行人信息包括执行法院、案件内容、执行标的、被执行人名称、组织机构代码等字段的详细信息
* path jr/zhixinginfo/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 历史被执行人


* method:  hi_zhixing
* name 历史被执行人
* desc 可以通过公司名称或ID获取企业历史的被执行人信息，历史被执行人信息包括执行法院、案件内容、执行标的、被执行人名称、组织机构代码等字段信息
* path hi/zhixing/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 失信人


* method:  jr_dishonest
* name 失信人
* desc 可以通过公司名称或ID判定企业失信情况，失信信息包括失信人名称、组织机构代码、履行情况、失信行为具体情形等字段的详细信息
* path jr/dishonest/2.0
* params ['name', 'id', 'keyword', 'pageNum']


#### 历史失信人


* method:  hi_dishonest
* name 历史失信人
* desc 可以通过公司名称或ID获取企业历史的失信情况，历史失信信息包括失信人名称、组织机构代码、履行情况、失信行为具体情形等字段信息
* path hi/dishonest/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 限制消费令


* method:  jr_consumptionRestriction
* name 限制消费令
* desc 可以通过公司名称或ID获取限制消费令信息，限制消费令信息包括执行法院、案件内容、被执行人名称等字段的详细信息
* path jr/consumptionRestriction/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 终本案件


* method:  jr_endCase
* name 终本案件
* desc 可以通过公司名称或ID获取终本案件信息，终本案件信息包括执行法院、案件内容、被执行人名称等字段的详细信息
* path jr/endCase/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 行政许可-工商局


* method:  m_getLicense
* name 行政许可-工商局
* desc 可以通过公司名称或ID获取企业行政许可信息，企业行政许可信息包括行政许可决定文书号、许可文件名称、许可机关等字段的详细信息
* path m/getLicense/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 历史行政许可-工商局


* method:  hi_license
* name 历史行政许可-工商局
* desc 可以通过公司名称或ID获取企业历史的行政许可信息，历史行政许可信息包括行政许可决定文书号、许可文件名称、许可机关等字段信息
* path hi/license/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 行政许可-其他来源


* method:  m_getLicenseCreditchina
* name 行政许可-其他来源
* desc 可以通过公司名称或ID获取企业行政许可信息，企业行政许可信息包括行政许可决定文书号、许可内容、许可机关、审核类型等字段的详细信息
* path m/getLicenseCreditchina/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 历史行政许可-其他来源


* method:  hi_license_creditChina
* name 历史行政许可-其他来源
* desc 可以通过公司名称或ID获取企业历史的行政许可信息，历史行政许可信息包括行政许可决定文书号、许可内容、许可机关、审核类型等字段信息
* path hi/license/creditChina/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 抽查检查


* method:  m_checkInfo
* name 抽查检查
* desc 可以通过公司名称或ID获取企业抽查检查信息，企业抽查检查信息包括类型、结果、实施机关等字段的详细信息
* path m/checkInfo/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 双随机抽查


* method:  m_doubleRandomCheck
* name 双随机抽查
* desc 可以通过公司名称或ID获取企业双随机抽查信息，企业双随机抽查信息包括抽查类型、抽查机关等字段的详细信息
* path m/doubleRandomCheck/2.0
* params ['id', 'name', 'pageNum', 'pageSize', 'keyword']


#### 双随机抽查详情


* method:  m_doubleRandomCheckDetail
* name 双随机抽查详情
* desc 可以通过双随机抽查ID获取企业双随机抽查详情，企业双随机抽查详情包括检查事项、检查结果等字段的详细信息
* path m/doubleRandomCheckDetail/2.0
* params ['businessId', 'pageNum', 'pageSize']


#### 税务评级


* method:  m_taxCredit
* name 税务评级
* desc 可以通过公司名称或ID获取企业税务评级信息，企业税务评级信息包括评价年度、纳税人信用级别、类型、纳税人识别号、评价单位等字段的详细信息
* path m/taxCredit/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 进出口信用


* method:  m_importAndExport
* name 进出口信用
* desc 可以通过公司名称或ID获取企业进出口信用信息，企业进出口信用信息包括海关注册编码、注册海关、经营类别等字段的详细信息
* path m/importAndExport/2.0
* params ['id', 'name', 'keyword']


#### 电信许可


* method:  m_teleCommunicationLicense
* name 电信许可
* desc 可以通过公司名称或ID获取企业电信许可信息，企业电信许可信息包括客户、销售占比、销售金额、报告期等字段的详细信息
* path m/teleCommunicationLicense/2.0
* params ['id', 'name', 'pageNum', 'pageSize', 'keyword']


#### 资质证书


* method:  m_certificate
* name 资质证书
* desc 可以通过公司名称或ID获取企业资质证书信息，企业资质证书信息包括证书类型、证书编号、发证日期等字段的详细信息
* path m/certificate/2.0
* params ['id', 'name', 'pageNum', 'certificateName', 'pageSize']


#### 公告研报


* method:  m_announcementReport
* name 公告研报
* desc 可以通过公司名称或ID获取企业研报和相关公告信息，企业研报和相关公告信息包括发布数量、发布日期、标题等字段的详细信息
* path m/announcementReport/2.0
* params ['id', 'name', 'pageNum', 'pageSize', 'type', 'keyword']


#### 企业信用评级


* method:  m_creditRating
* name 企业信用评级
* desc 可以通过公司名称或ID获取企业信用评级信息，企业信用评级信息包括评级公司、主体等级、债券信用等级、评级展望、评级时间等字段的信息
* path m/creditRating/2.0
* params ['id', 'name', 'pageNum', 'pageSize', 'keyword']


#### 一般纳税人


* method:  m_taxpayer
* name 一般纳税人
* desc 可以通过公司名称或ID获取一般纳税人信息，一般纳税人信息包括纳税人名称、纳税人识别号、纳税人资格类型、主管税务机关、有效期起、有效期止等字段的信息
* path m/taxpayer/2.0
* params ['id', 'name', 'pageNum', 'pageSize', 'keyword']


#### 债券信息


* method:  m_bond
* name 债券信息
* desc 可以通过公司名称或ID获企业发行债券信息，债券信息包括发行日期、债券名称、债券代码、债券类型等字段的详细信息
* path m/bond/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 产品信息


* method:  m_appbkInfo
* name 产品信息
* desc 可以通过公司名称或ID获取企业产品信息，企业产品信息包括主要产品、产品分类、产品介绍等字段的详细信息
* path m/appbkInfo/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 购地信息


* method:  m_purchaseLand
* name 购地信息
* desc 可以通过公司名称或ID获取企业购地信用信息，企业购地信用信息包括土地坐落、土地用途、总面积、供应方式等字段的详细信息
* path m/purchaseLand/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 供应商


* method:  m_supply
* name 供应商
* desc 可以通过公司名称或ID获取企业相关供应商信息，企业相关供应商信息包括供应商、采购占比、采购金额、报告期等字段的详细信息
* path m/supply/2.0
* params ['id', 'name', 'pageNum', 'pageSize', 'year', 'keyword']


#### 客户


* method:  m_customer
* name 客户
* desc 可以通过公司名称或ID获取企业相关客户信息，企业相关客户信息包括客户、销售占比、销售金额、报告期等字段的详细信息
* path m/customer/2.0
* params ['id', 'name', 'pageNum', 'pageSize', 'year', 'keyword']


#### 企业招聘


* method:  m_employments
* name 企业招聘
* desc 可以通过公司名称或ID获取企业招聘相关信息，企业招聘相关信息包括发布日期、招聘职位、月薪、学历、地区等字段的详细信息
* path m/employments/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 企业招聘-百聘


* method:  m_bp_employments
* name 企业招聘-百聘
* desc 可以通过公司名称或ID获取企业招聘相关信息，企业招聘相关信息包括发布日期、招聘职位、月薪、学历、地区等字段的详细信息
* path m/bp/employments/2.0
* params ['id', 'name', 'pageNum', 'pageSize', 'keyword']


#### 企业微博


* method:  m_weibo
* name 企业微博
* desc 可以通过公司名称或ID获取企业微博的有关信息，包括企业微博名称、行业类别、简介等字段的详细信息
* path m/weibo/2.0
* params ['id', 'name', 'pageNum', 'pageSize', 'keyword']


#### 企业微信公众号


* method:  ipr_publicWeChat
* name 企业微信公众号
* desc 可以通过公司名称或ID获取企业微信公众号的有关信息，包括企业微信公众号名称、微信号、二维码、功能介绍等字段的详细信息
* path ipr/publicWeChat/2.0
* params ['id', 'name', 'pageNum']


#### 企业招投标信息


* method:  m_bids
* name 企业招投标信息
* desc 可以通过公司名称或ID获企业招投标信息，招投标信息包括采购人、发布时间、正文信息等字段的详细信息
* path m/bids/2.0
* params ['id', 'name', 'keyword', 'pageSize', 'pageNum', 'type', 'province', 'publishStartTime', 'publishEndTime']


#### 招投标信息垂搜


* method:  m_bids_search
* name 招投标信息垂搜
* desc 通过招投标标题、采购人、公告类型等方式，查询招投标的有关信息
* path m/bids/search
* params ['keyword', 'searchType', 'publishStartTime', 'type', 'province', 'publishEndTime', 'pageNum', 'pageSize']


#### 地块公示


* method:  m_landPublicity
* name 地块公示
* desc 可以通过公司名称或ID获取企业地块公示信息，企业地块公示信息包括地块位置、土地用途、面积、发布机关等字段的详细信息
* path m/landPublicity/2.0
* params ['id', 'name', 'pageNum', 'pageSize', 'keyword']


#### 地块公示详情


* method:  m_landPublicity_detail
* name 地块公示详情
* desc 可以通过地块公示ID获取企业地块公示详情，企业地块公示详情包括地块位置、土地用途、面积、发布机关、联系方式等字段的详细信息
* path m/landPublicity/detail/2.0
* params ['id']


#### 土地转让


* method:  m_landTransfer
* name 土地转让
* desc 可以通过公司名称或ID获取企业土地转让信息，企业土地转让信息包括土地坐落、原/现土地使用人、面积、转让价格等字段的详细信息
* path m/landTransfer/2.0
* params ['id', 'name', 'pageNum', 'pageSize', 'keyword']


#### 土地转让详情


* method:  m_landTransfer_detail
* name 土地转让详情
* desc 可以通过土地转让ID获取企业土地转让详情，企业土地转让详情包括土地坐落、原/现土地使用人、面积、转让价格、转让方式等字段的详细信息
* path m/landTransfer/detail/2.0
* params ['id']


#### 行政处罚-工商局


* method:  mr_punishmentInfo
* name 行政处罚-工商局
* desc 可以通过公司名称或ID获取企业行政处罚信息，行政处罚信息包括行政处罚明细、行政处罚公告、行政处罚内容、公示日期等字段的详细信息
* path mr/punishmentInfo/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 历史行政处罚-工商局


* method:  hi_punishment
* name 历史行政处罚-工商局
* desc 可以通过公司名称或ID获取企业历史的行政处罚信息，历史行政处罚信息包括行政处罚明细、行政处罚公告、行政处罚内容、公示日期等字段信息
* path hi/punishment/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 行政处罚-其他来源


* method:  mr_creditChina
* name 行政处罚-其他来源
* desc 可以通过公司名称或ID获取企业行政处罚信息，行政处罚信息包括行政处罚明细、行政处罚公告、行政处罚内容、公示日期、处罚依据、处罚状态等字段的详细信息
* path mr/creditChina/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 历史行政处罚-其他来源


* method:  hi_punishment_creditChina
* name 历史行政处罚-其他来源
* desc 可以通过公司名称或ID获取企业历史的行政处罚信息，历史行政处罚信息包括行政处罚明细、行政处罚公告、行政处罚内容、公示日期、处罚依据、处罚状态等字段信息
* path hi/punishment/creditChina/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 欠税公告


* method:  mr_ownTax
* name 欠税公告
* desc 可以通过公司名称或ID获取企业欠税信息，企业欠税信息包括欠税公告、纳税人识别号、证件号码、经营地点、欠税税种、欠税余额等字段的详细信息
* path mr/ownTax/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 税收违法


* method:  mr_taxContravention
* name 税收违法
* desc 可以通过公司名称或ID获取税收违法信息，税收违法信息包括纳税人名称、案件性质等字段的详细信息
* path mr/taxContravention/2.0
* params ['id', 'name', 'pageNum', 'pageSize', 'keyword']


#### 税收违法详情


* method:  mr_taxContravention_detail
* name 税收违法详情
* desc 根据税收违法ID获取税收违法详情，税收违法详情包括纳税人名称、纳税人识别号、注册地址、违法事实、财务负责人信息、负有责任的中介信息等字段的详细信息
* path mr/taxContravention/detail/2.0
* params ['id']


#### 经营异常


* method:  mr_abnormal
* name 经营异常
* desc 可以通过公司名称或ID获取企业经营异常信息，经营异常信息包括列入/移除原因、时间、做出决定机关等字段的详细信息
* path mr/abnormal/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 历史经营异常


* method:  hi_abnormal
* name 历史经营异常
* desc 可以通过公司名称或ID获取企业历史的经营异常信息，历史经营异常信息包括列入/移除原因、时间、做出决定机关等字段信息
* path hi/abnormal/2.0
* params ['id', 'name', 'pageNum', 'pageSize', 'keyword']


#### 严重违法


* method:  mr_illegalinfo
* name 严重违法
* desc 可以通过公司名称或ID获取企业严重违法信息，严重违法信息包括列入/移除原因、时间、做出决定机关等字段的详细信息
* path mr/illegalinfo/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 清算信息


* method:  mr_liquidating
* name 清算信息
* desc 可以通过公司名称或ID获取企业清算信息，企业清算信息包括清算组负责人、清算组成员
* path mr/liquidating/2.0
* params ['id', 'name', 'keyword']


#### 简易注销


* method:  mr_briefCancel
* name 简易注销
* desc 可以通过公司名称或ID获取企业简易注销公告信息，企业简易注销公告信息包括全体投资人承诺书、异议信息、简易注销结果等字段的详细信息
* path mr/briefCancel/2.0
* params ['id', 'name', 'keyword']


#### 询价评估


* method:  mr_inquiryEvaluation
* name 询价评估
* desc 可以通过公司名称或ID获取询价评估信息，询价评估信息包括标的物名称、当事人姓名、评估机构名称等字段的详细信息
* path mr/inquiryEvaluation/2.0
* params ['id', 'name', 'pageNum', 'pageSize', 'keyword']


#### 司法拍卖


* method:  mr_judicialSale
* name 司法拍卖
* desc 可以通过公司名称或ID获取企业司法拍卖公告信息，企业司法拍卖公告信息包括拍卖公告标题、执行法院、拍卖时间、拍卖标的、起拍价格等字段的详细信息
* path mr/judicialSale/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 公示催告


* method:  _services_v4_open_publicNotice
* name 公示催告
* desc 可以通过公司名称或ID获取企业票据公示催告信息，企业票据公示催告信息包括票据公示催告详情、票据号、票据类型、票面金额、公告日期、公告内容等字段的详细信息
* path /services/v4/open/publicNotice
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 动产抵押


* method:  mr_mortgageInfo
* name 动产抵押
* desc 可以通过公司名称或ID获取企业动产抵押公告信息，企业动产抵押公告信息包括被担保债权类型、数额、登记机关等字段信息
* path mr/mortgageInfo/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 历史动产抵押


* method:  hi_mortgageInfo
* name 历史动产抵押
* desc 可以通过公司名称或ID获取企业历史的动产抵押公告信息，历史动产抵押公告信息包括被担保债权类型、数额、登记机关等字段信息
* path hi/mortgageInfo/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 土地抵押


* method:  mr_landMortgage
* name 土地抵押
* desc 可以通过公司名称或ID获取企业土地抵押信息、企业土地抵押信息包括土地坐落、抵押面积、抵押土地用途等字段的详细信息
* path mr/landMortgage/2.0
* params ['id', 'name', 'pageNum', 'pageSize', 'keyword']


#### 土地抵押详情


* method:  mr_landMortgage_detail
* name 土地抵押详情
* desc 根据土地抵押ID获取土地抵押详情，土地抵押详情包括抵押面积、土地抵押人名称、抵押土地用途、评估金额、抵押金额、抵押人等字段的详细信息
* path mr/landMortgage/detail/2.0
* params ['id']


#### 知识产权出质


* method:  _services_v4_open_getPledgeReg
* name 知识产权出质
* desc 可以通过公司名称或ID获取知识产权出质信息，知识产权出质信息包括质权人名称、知识产权登记证号等字段的详细信息
* path /services/v4/open/getPledgeReg
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 股权出质


* method:  mr_equityInfo
* name 股权出质
* desc 可以通过公司名称或ID获取出质股权标的企业信息，包括企业质权人信息、出质人信息、出质股权数额等字段的详细信息
* path mr/equityInfo/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 历史股权出质


* method:  hi_equityInfo
* name 历史股权出质
* desc 可以通过公司名称或ID获取历史出质股权标的企业信息，包括历史质权人信息、出质人信息、出质股权数额等字段信息
* path hi/equityInfo/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 质押明细


* method:  mr_stockPledge_detailList
* name 质押明细
* desc 可以通过公司名称或ID获取股权质押明细信息，股权质押走势信息包括股东名称、质押股份数量、质押股份市值等字段的详细信息
* path mr/stockPledge/detailList/2.0
* params ['id', 'name', 'pageNum', 'pageSize', 'keyword']


#### 质押明细详情


* method:  mr_stockPledge_detail
* name 质押明细详情
* desc 根据质押明细ID获取股权质押明细详情，股权质押明细详情包括股东名称、质押股份数量、质押股份市值、占所持股份比例、质押机构、质押原因等字段的详细信息
* path mr/stockPledge/detail/2.0
* params ['businessId', 'id']


#### 重要股东质押


* method:  mr_stockPledge_shareholder
* name 重要股东质押
* desc 可以通过公司名称或ID获取重要股东质押统计（质押中）信息，重要股东质押统计（质押中）信息包括股东名称、最新质押笔数、剩余质押股数（股）等字段的详细信息
* path mr/stockPledge/shareholder/2.0
* params ['id', 'name', 'pageNum', 'pageSize', 'keyword']


#### 重要股东质押详情


* method:  mr_stockPledge_shareholder_detail
* name 重要股东质押详情
* desc 根据重要股东质押统计（质押中）ID获取重要股东质押统计（质押中）详情，重要股东质押统计（质押中）详情包括股东名称、最新质押笔数、剩余质押股数等字段的详细信息
* path mr/stockPledge/shareholder/detail/2.0
* params ['businessId', 'id']


#### 质押比例


* method:  mr_stockPledge_ratio
* name 质押比例
* desc 可以通过公司名称或ID获取股权质押比例信息，股权质押比例信息包括股票代码、近一年涨跌幅、质押比例、质押股数、质押市值、质押笔数等字段的详细信息
* path mr/stockPledge/ratio/2.0
* params ['id', 'name', 'date', 'keyword']


#### 质押走势


* method:  mr_stockPledge_trend
* name 质押走势
* desc 可以通过公司名称或ID获取股权质押明细信息，股权质押走势信息包括股东名称、质押股份数量、质押股份市值等字段的详细信息
* path mr/stockPledge/trend/2.0
* params ['name', 'id', 'keyword']


#### 企业商标信息


* method:  ipr_tm
* name 企业商标信息
* desc 可以通过公司名称或ID获取商标的有关信息，包括商标图片、注册号、国际分类等字段的详细信息
* path ipr/tm/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize', 'tmClass', 'status', 'appDateBegin', 'appDateEnd']


#### 历史商标信息


* method:  hi_tm
* name 历史商标信息
* desc 可以通过公司名称或ID获取历史的商标有关信息，历史商标信息包括商标图片、注册号、国际分类等字段信息
* path hi/tm/2.0
* params ['id', 'name', 'pageNum', 'pageSize', 'keyword']


#### 商标信息垂搜


* method:  ipr_tm_search
* name 商标信息垂搜
* desc 通过商标名称、注册号、申请人、商标分类等方式，查询商标的有关信息
* path ipr/tm/search
* params ['keyword', 'searchType', 'tmClass', 'status', 'appDateBegin', 'appDateEnd', 'pageNum', 'pageSize']


#### 商标信息详情


* method:  ipr_tm_detail
* name 商标信息详情
* desc 可以通过注册号或国际分类获取商标信息详情，商标信息详情包括商标国际分类、商标名称、商标申请日期、商标申请人、商标注册地址、商标合作申请人、商标申请人（英文）、商标地址（英文）、商标初审公告期号、商标初审公告日期、商标注册公告期号、商标注册公告日期、商标专用权期限期限、商标代理/办理机构等字段的信息
* path ipr/tm/detail/2.0
* params ['regNo', 'intCls']


#### 企业专利信息


* method:  ipr_patents
* name 企业专利信息
* desc 可以通过公司名称或ID获取专利的有关信息，包括专利名称、申请号、申请公布号等字段的详细信息
* path ipr/patents/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize', 'patentType', 'pubDateBegin', 'pubDateEnd', 'appDateBegin', 'appDateEnd']


#### 专利信息垂搜


* method:  ipr_patents_search
* name 专利信息垂搜
* desc 通过专利名称、申请号、申请人、专利分类等方式，查询专利的有关信息
* path ipr/patents/search
* params ['keyword', 'searchType', 'patentType', 'pubDateBegin', 'pubDateEnd', 'appDateBegin', 'appDateEnd', 'pageNum', 'pageSize']


#### 软件著作权


* method:  ipr_copyReg
* name 软件著作权
* desc 可以通过公司名称或ID获取软件著作权的有关信息，包括软件名称、登记号、分类号、版本号等字段的详细信息
* path ipr/copyReg/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 作品著作权


* method:  ipr_copyRegWorks
* name 作品著作权
* desc 可以通过公司名称或ID获取作品著作权的有关信息，包括作品名称、登记号、登记类别等字段的详细信息
* path ipr/copyRegWorks/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 网站备案


* method:  ipr_icp_3.0
* name 网站备案
* desc 可以通过公司名称或ID获取网站备案的有关信息，包括网站名称、网站首页、域名、网站备案/许可证号等字段信息
* path ipr/icp/3.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 历史网站备案


* method:  hi_icp
* name 历史网站备案
* desc 可以通过公司名称或ID获取历史的网站备案有关信息，历史网站备案信息包括网站名称、网站首页、域名、网站备案/许可证号等字段信息
* path hi/icp/2.0
* params ['id', 'name', 'pageNum', 'pageSize', 'keyword']


#### 人员控股企业


* method:  human_companyholding
* name 人员控股企业
* desc 可以通过公司名称、人名获取人员控股企业信息，人员控股企业信息包括控股企业ID、投资比例、企业logo、企业简称、控股企业、注册资本、法人类型、经营状态、法人等字段的信息
* path human/companyholding/2.0
* params ['name', 'humanName', 'cid', 'hid', 'pageNum', 'pageSize']


#### 人员所有角色


* method:  _services_v4_open_roles
* name 人员所有角色
* desc 可以通过公司名称或ID和人名获取人员的所有商业角色，包括其担任法人、股东、董监高的职位信息
* path /services/v4/open/roles
* params ['name', 'humanName', 'cid', 'hid']


#### 人员所有公司


* method:  _services_v4_open_allCompanys
* name 人员所有公司
* desc 可以通过公司名称或ID和人名获取企业人员的所有相关公司，包括其担任法人、股东、董监高的公司信息
* path /services/v4/open/allCompanys
* params ['name', 'humanName', 'cid', 'hid']


#### 人员所有合作伙伴


* method:  _services_v4_open_partners
* name 人员所有合作伙伴
* desc 可以通过公司名称或ID和人名获取人员的所有合作伙伴，包括其合作伙伴的所有相关公司数量、公司名称或ID信息
* path /services/v4/open/partners
* params ['name', 'humanName', 'cid', 'hid']


#### 企业人员简介


* method:  _services_v4_open_description
* name 企业人员简介
* desc 可以通过公司名称或ID和人名获取人员简介信息
* path /services/v4/open/description
* params ['name', 'humanName', 'cid', 'hid']


#### 企业图谱


* method:  _services_v4_open_oneKey_c
* name 企业图谱
* desc 可以通过公司ID获取企业关系图谱，包含法人、股东、高管、对外投资、分支机构列表
* path /services/v4/open/oneKey/c
* params ['id', 'name', 'keyword']


#### 股权结构图


* method:  _services_v4_open_equityRatio
* name 股权结构图
* desc 可以通过公司ID获取企业股权控制结构及疑似实际控制人
* path /services/v4/open/equityRatio
* params ['id', 'name', 'keyword']


#### 股权穿透图


* method:  _services_v3_open_investtree
* name 股权穿透图
* desc 可以通过公司ID获取企业上下游对外投资关系，包含持股比例、直接与间接投资企业等
* path /services/v3/open/investtree
* params ['id', 'flag', 'dir', 'name', 'keyword']


#### 最终受益人


* method:  ic_humanholding
* name 最终受益人
* desc 可以通过公司名称或ID获取股权向上穿透后识别的企业最终受益人，包含（一名或多名）股东姓名、持股比例，层级关系等
* path ic/humanholding/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 实际控制权


* method:  _services_v4_open_companyholding
* name 实际控制权
* desc 可以通过公司名称或ID获取股权向下穿透后识别的当前企业实际控制的企业，包括对应公司名称或ID、出资比例、投资链等
* path /services/v4/open/companyholding
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 疑似实际控制人


* method:  ic_actualControl
* name 疑似实际控制人
* desc 可以通过公司名称或ID获取股权向上穿透后识别的企业疑似实际控制人，包含（一名）疑似控制人姓名、层级关系等字段信息
* path ic/actualControl/2.0
* params ['name', 'id', 'keyword']


#### 最短路径发现


* method:  rela_shortPath
* name 最短路径发现
* desc 可以通过公司A，公司B，关系类型（法人/任职/投资/分支/诉讼/竞合/债务，可多选）查询两家公司之间是否存在关联关系
* path rela/shortPath
* params ['nameFrom', 'idFrom', 'nameTo', 'idTo', 'depth', 'types']


#### 新闻舆情


* method:  ps_news
* name 新闻舆情
* desc 根据公司id或公司名称（精确匹配）获取新闻列表
* path ps/news/2.0
* params ['name', 'id', 'startTime', 'endTime', 'pageNum', 'pageSize', 'tags']


#### 企业天眼风险


* method:  risk_riskInfo
* name 企业天眼风险
* desc 可以通过公司名称或ID获取企业相关天眼风险列表，包括企业自身/周边/预警风险信息
* path risk/riskInfo/2.0
* params ['id', 'name', 'keyword']


#### 天眼地图


* method:  _services_v4_open_proximity
* name 天眼地图
* desc 附近公司
* path /services/v4/open/proximity
* params ['pageNum', 'pageSize', 'distance', 'longtitude', 'latitude', 'regStatus']


#### 人员天眼风险


* method:  _services_v4_open_humanRiskInfo
* name 人员天眼风险
* desc 可以通过公司名称或ID和人名获取人员相关天眼风险列表，包括人员周边/预警风险信息
* path /services/v4/open/humanRiskInfo
* params ['name', 'humanName', 'cid', 'hid']


#### 天眼风险详情


* method:  _services_v4_open_riskDetail
* name 天眼风险详情
* desc 可以通过企业风险ID和人风险ID获取企业或人员相关天眼风险详情，包括企业和人员自身/周边/预警风险信息详情
* path /services/v4/open/riskDetail
* params ['id', 'pageSize', 'pageNum', 'type']


#### 企业无水印logo


* method:  _services_v4_open_logo
* name 企业无水印logo
* desc 可以通过公司名称获取公司无水印logo
* path /services/v4/open/logo
* params ['id', 'name', 'keyword']


#### 验证企业


* method:  _services_v4_open_match
* name 验证企业
* desc 可以查询公司名称或ID和企业信用代码是否对应
* path /services/v4/open/match
* params ['name', 'keyword']


#### 企业经纬度


* method:  _services_v4_open_position
* name 企业经纬度
* desc 可以通过公司名称或ID获取企业经纬度信息
* path /services/v4/open/position
* params ['id', 'name', 'keyword']


#### 企业曾用名


* method:  _services_v4_open_historyNames
* name 企业曾用名
* desc 可以通过公司名称获取企业曾用名
* path /services/v4/open/historyNames
* params ['id', 'name', 'keyword']


#### 纳税人识别号


* method:  _services_v4_open_taxesCode
* name 纳税人识别号
* desc 可以通过公司名称获取企业纳税人识别号
* path /services/v4/open/taxesCode
* params ['id', 'name', 'keyword']


#### 按行业/区域查询公司


* method:  _services_v4_open_searchV3
* name 按行业/区域查询公司
* desc 可以通过关键词、行业、省市区获取企业列表，企业列表包括公司名称或ID、类型、成立日期、经营状态、统一社会信用代码等字段的详细信息
* path /services/v4/open/searchV3
* params ['word', 'pageNum', 'categoryGuobiao', 'areaCode']


#### 企业简介


* method:  _services_v4_open_profile
* name 企业简介
* desc 可以通过公司名称或ID获取企业简介信息
* path /services/v4/open/profile
* params ['id', 'name', 'keyword']


#### 企业信用报告（基础版）


* method:  report_company_base
* name 企业信用报告（基础版）
* desc 可以通过公司名称或ID获取企业信用报告(基础版)，基础版企业信用报告包括工商信息、分支机构、变更记录、主要人员、联系方式、股东信息、对外投资信息、风险信息、知识产权信息、经营信息、年报信息、财务信息等字段的详细信息
* path report/company/base
* params ['id', 'name', 'uuid']


#### 企业信用报告（专业版）


* method:  report_company_pro
* name 企业信用报告（专业版）
* desc 可以通过公司名称或ID获取企业信用报告(专业版)，专业版企业信用报告包括工商信息、分支机构、变更记录、主要人员、联系方式、控股企业、股东信息、对外投资信息、股权控制路径、风险信息、知识产权信息、经营信息、年报信息、财务信息等字段的详细信息
* path report/company/pro
* params ['id', 'name', 'uuid']


#### 工商信息


* method:  cb_ic
* name 工商信息
* desc 可以通过公司名称或ID获取包含企业简介、企业基本信息、主要人员、股东信息、对外投资、分支机构等维度的相关信息
* path cb/ic/2.0
* params ['id', 'name', 'keyword']


#### 司法风险


* method:  cb_judicial
* name 司法风险
* desc 可以通过公司名称或ID获取包含法律诉讼、法院公告、开庭公告、失信人、被执行人、司法协助、立案信息、送达公告、终本案件、限制消费令等维度的相关信息
* path cb/judicial/2.0
* params ['id', 'name', 'keyword']


#### 知识产权


* method:  cb_ipr
* name 知识产权
* desc 可以通过公司名称或ID获取包含商标、专利、作品著作权、软件著作权、网站备案等维度的相关信息
* path cb/ipr/2.0
* params ['id', 'name', 'keyword']


#### 企业发展


* method:  cb_development
* name 企业发展
* desc 可以通过公司名称或ID获取包含核心团队、企业业务、融资历史、投资事件、竞品信息、相关项目品牌/投资机构、投资动态等维度的相关信息
* path cb/development/2.0
* params ['id', 'name', 'keyword']


#### 历史信息


* method:  cb_history
* name 历史信息
* desc 可以通过公司名称或ID获取包含历史工商信息、历史股东信息、历史对外投资、历史行政许可、历史法律诉讼、历史法院公告、历史开庭公告、历史司法协助、历史失信人、历史被执行人、历史经营异常、历史股权出质、历史动产抵押、历史行政处罚、历史商标信息、历史网站备案等维度的相关信息
* path cb/history/2.0
* params ['id', 'name', 'keyword']


#### 投资动态


* method:  _services_v4_open_investEvent
* name 投资动态
* desc 可以通过投资机构名称获取投资产品名称、产品logo、投资金额、融资轮次、相关新闻等字段的详细信息
* path /services/v4/open/investEvent
* params ['name', 'pageNum', 'pageSize']


#### 融资历史


* method:  cd_findHistoryRongzi
* name 融资历史
* desc 可以通过公司名称或ID获取企业融资历史信息，企业融资历史信息包括融资轮次、交易金额、估值、投资方等字段的详细信息
* path cd/findHistoryRongzi/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 核心团队


* method:  cd_findTeamMember
* name 核心团队
* desc 可以通过公司名称或ID获取企业核心团队信息，企业核心团队信息包括核心人员姓名、职位、过往经历简介等字段的详细信息
* path cd/findTeamMember/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 企业业务


* method:  cd_getProductInfo
* name 企业业务
* desc 可以通过公司名称或ID获取企业业务信息，企业业务信息包括主要业务、业务分类、业务介绍等字段的详细信息
* path cd/getProductInfo/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 投资事件


* method:  cd_findTzanli
* name 投资事件
* desc 可以通过公司名称或ID获取企业投资事件信息，企业投资事件信息包括投资事件轮次、金额、投资方、投资产品、行业、业务等字段的详细信息
* path cd/findTzanli/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 竞品信息


* method:  cd_findJingpin
* name 竞品信息
* desc 可以通过公司名称或ID获取企业竞品信息，企业竞品信息包括竞品名称、行业、业务等字段的详细信息
* path cd/findJingpin/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 获取标签


* method:  cd_tags
* name 获取标签
* desc 可以通过品牌ID获取企业标签，企业标签包括领域分类、主营业务、榜单等
* path cd/tags/2.0
* params ['id']


#### 搜索项目品牌/投资机构


* method:  cd_searchBrandAndAgency
* name 搜索项目品牌/投资机构
* desc 可以通过关键词获取项目品牌和投资机构信息，包括项目品牌和投资机构名称、logo、融资轮次或投资事件等字段的详细信息
* path cd/searchBrandAndAgency/2.0
* params ['word']


#### 投资机构


* method:  cd_investOrg
* name 投资机构
* desc 可以通过公司名称或ID获企业相关投资机构信息，投资机构信息包括机构名称、成立日期、简介等字段的详细信息
* path cd/investOrg/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 私募基金


* method:  cd_privateFund
* name 私募基金
* desc 可以通过公司名称或ID获企业相关私募基金信息，私募基金信息包括私募基金管理人名称、法定代表人/执行事务合伙人、机构类型、登记编号等字段的详细信息
* path cd/privateFund/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 上市公司财务简析


* method:  _services_v4_open_financialAnalysis
* name 上市公司财务简析
* desc 可以通过公司名称或ID获取上市公司财务简析数据，上市公司财务简析数据包括营业收入、净利润、总资产、净资产、净利率、毛利率等
* path /services/v4/open/financialAnalysis
* params ['id', 'name', 'keyword']


#### 股票行情


* method:  stock_volatility
* name 股票行情
* desc 可以通过公司名称或ID获取上市公司股票行情数据，上市公司股票行情数据包括股票名、股票号、总市值、流通市值等
* path stock/volatility/2.0
* params ['name', 'id', 'keyword']


#### 上市公司企业简介


* method:  stock_companyInfo
* name 上市公司企业简介
* desc 可以通过公司名称或ID获取上市公司企业简介，上市公司企业简介包括公司全称、曾用名、工商登记号、注册资本、所属行业、主要人员、控股股东、实际控制人、最终控制人、主营业务等
* path stock/companyInfo/2.0
* params ['id', 'name', 'keyword']


#### 高管信息


* method:  stock_seniorExecutive
* name 高管信息
* desc 可以通过公司名称或ID获取上市公司高管信息，上市公司高管信息包括高管姓名、职务、持股数、年龄、学历等
* path stock/seniorExecutive/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 参股控股


* method:  stock_holdingCompany
* name 参股控股
* desc 可以通过公司名称或ID获取上市公司参股控股股东信息，参股控股股东信息包括参股控股关联公司、参股关系、参股比例、投资金额、被参股公司净利润等
* path stock/holdingCompany/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 上市公告


* method:  stock_announcement
* name 上市公告
* desc 可以通过公司名称或ID获取上市公司上市公告信息，上市公告信息包括公告标题、发布日期、股票名、股票号等
* path stock/announcement/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 十大股东（十大流通股东）


* method:  stock_shareholder
* name 十大股东（十大流通股东）
* desc 可以通过公司名称或ID获取上市公司十大股东和十大流通股东信息，十大股东和十大流通股东信息包括机构或基金、持有数量、持股变化、占股本比例、实际增减持、股份类型等
* path stock/shareholder/2.0
* params ['id', 'keyword', 'type', 'name', 'time']


#### 发行相关


* method:  stock_issueRelated
* name 发行相关
* desc 可以通过公司名称或ID获取上市公司发行相关信息，发行相关信息包括成立日期、上市日期、发行数量、发行价格等
* path stock/issueRelated/2.0
* params ['id', 'name', 'keyword']


#### 股本结构


* method:  stock_shareStructure
* name 股本结构
* desc 可以通过公司名称或ID获取上市公司股本结构信息，股本结构信息包括总股本、A股总股本、流通A股、限售A股等
* path stock/shareStructure/2.0
* params ['id', 'name', 'keyword', 'time']


#### 股本变动


* method:  stock_equityChange
* name 股本变动
* desc 可以通过公司名称或ID获取上市公司股本变动信息，股本变动信息包括变动时间、变动原因、变动后A股总股本、变动后流通A股、变动后限售A股等
* path stock/equityChange/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 分红情况


* method:  stock_bonusInfo
* name 分红情况
* desc 可以通过公司名称或ID获取上市公司分红情况信息，分红情况信息包括董事会日期、股东大会日期、实施日期、分红方案说明、分红率等
* path stock/bonusInfo/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 配股情况


* method:  stock_allotmen
* name 配股情况
* desc 可以通过公司名称或ID获取上市公司配股情况信息，配股情况信息包括方案进度、配股代码、配股简称、实际配股比例、每套配股价格、实际募集资金净额等
* path stock/allotmen/2.0
* params ['id', 'name', 'keyword', 'pageNum', 'pageSize']


#### 证券信息


* method:  stock_security
* name 证券信息
* desc 可以通过公司名称或ID获取上市公司证券信息，证券信息包括A股代码、A股简称、律师事务所、会计师事务所、股票类型等
* path stock/security/2.0
* params ['id', 'name', 'keyword']


#### 重要人员


* method:  stock_corpBasicInfo
* name 重要人员
* desc 可以通过公司名称或ID获取上市公司重要人员信息，重要人员信息包括总经理、法人代表、董秘、董事长、证券事务代表、独立董事等
* path stock/corpBasicInfo/2.0
* params ['id', 'name', 'keyword']


#### 联系信息


* method:  stock_corpContactInfo
* name 联系信息
* desc 可以通过公司名称或ID获取上市公司联系信息，联系信息包括联系电话、电子邮箱、传真、公司网址、办公地址、注册地址等
* path stock/corpContactInfo/2.0
* params ['id', 'name', 'keyword']


#### 主要指标-年度


* method:  stock_mainIndex
* name 主要指标-年度
* desc 可以通过公司名称或ID获取上市公司年度主要指标数据，年度主要指标数据包括基本每股收益、扣非每股收益、稀释每股收益、每股净资产、每股公积金等
* path stock/mainIndex/2.0
* params ['id', 'name', 'keyword']


#### 主要指标-季度


* method:  stock_quarMainIndex
* name 主要指标-季度
* desc 可以通过公司名称或ID获取上市公司季度主要指标数据，季度主要指标数据包括基本每股收益、扣非每股收益、稀释每股收益、每股净资产、每股公积金等
* path stock/quarMainIndex/2.0
* params ['id', 'name', 'year', 'keyword']


#### 对外担保


* method:  stock_guarantees
* name 对外担保
* desc 可以通过公司名称或ID获取上市公司对外担保信息，对外担保信息包括公告日期、担保方、被担保方、担保方式、担保金额等
* path stock/guarantees/2.0
* params ['id', 'name', 'pageNum', 'pageSize', 'keyword']


#### 违规处理


* method:  stock_illegal
* name 违规处理
* desc 可以通过公司名称或ID获取上市公司违规处理信息，违规处理信息包括公告日期、处罚对象、处罚类型、处罚金额、处理人等
* path stock/illegal/2.0
* params ['id', 'name', 'pageNum', 'pageSize', 'keyword']


#### 利润表


* method:  stock_profit
* name 利润表
* desc 可以通过公司名称或ID获取上市公司利润表数据，利润表数据包括营业总收入、营业总成本、其他经营收益、营业利润等
* path stock/profit/2.0
* params ['id', 'name', 'year', 'keyword']


#### 资产负债表


* method:  stock_balanceSheet
* name 资产负债表
* desc 可以通过公司名称或ID获取上市公司资产负债表数据，资产负债表数据包括流动资产、流动资产合计、非流动资产等
* path stock/balanceSheet/2.0
* params ['id', 'name', 'year', 'keyword']


#### 现金流量表


* method:  stock_cashFlow
* name 现金流量表
* desc 可以通过公司名称或ID获取上市公司现金流量表数据，现金流量表数据包括经营活动产生的现金流量、经营活动现金流小计、经营活动现金流出小计、经营活动产生的现金流量净额、投资活动产生的现金流量等
* path stock/cashFlow/2.0
* params ['id', 'name', 'year', 'keyword']


#### 招股书


* method:  stock_prospectus
* name 招股书
* desc 可以通过公司名称或ID获取上市公司招股书信息，招股书信息包括招股书标题、股票名称、招股书内容等
* path stock/prospectus/2.0
* params ['id', 'name', 'keyword']


#### 工商追踪


* method:  oi_businessEvent
* name 工商追踪
* desc 可以通过投资机构名称获取被投资企业名称、logo、投资比例等字段的详细信息
* path oi/businessEvent/2.0
* params ['name', 'pageNum', 'pageSize']


#### 相关新闻


* method:  oi_news
* name 相关新闻
* desc 可以通过投资机构名称获取相关新闻舆情信息，包括发稿媒体、新闻标题、发布时间、网址链接等字段的详细信息
* path oi/news/2.0
* params ['name', 'pageNum', 'pageSize']


#### 机构成员


* method:  oi_team
* name 机构成员
* desc 可以通过投资机构名称获取机构成员信息，机构成员信息包括成员姓名、职位、简介等字段的详细信息
* path oi/team/2.0
* params ['name', 'pageNum', 'pageSize']


#### 公开投资事件


* method:  oi_publicInvest
* name 公开投资事件
* desc 可以通过投资机构名称获取公开投资产品，包括产品名称、所属公司、参与轮次、投资时间、投资金额、产品介绍等字段的详细信息
* path oi/publicInvest/2.0
* params ['name', 'pageNum', 'pageSize']


#### 未公开投资


* method:  oi_secretInvest
* name 未公开投资
* desc 可以通过投资机构名称获取未公开投资企业，包括企业名称、法人、注册资本、成立日期、投资方等字段的详细信息
* path oi/secretInvest/2.0
* params ['name', 'pageNum', 'pageSize']


#### 管理基金


* method:  oi_funds
* name 管理基金
* desc 可以通过投资机构名称获取投资机构管理基金信息，包括企业名称、法定代表人、注册资本、成立日期等字段信息
* path oi/funds/2.0
* params ['name', 'pageNum', 'pageSize']


####  对外投资基金


* method:  oi_extFunds
* name  对外投资基金
* desc 可以通过投资机构名称获取投资机构对外投资基金信息，包括企业名称、法人、注册资本、成立日期、投资方等字段信息
* path oi/extFunds/2.0
* params ['name', 'pageNum', 'pageSize']


#### 基金管理人


* method:  oi_fundManager
* name 基金管理人
* desc 可以通过投资机构名称获取投资机构基金管理人信息，包括基金管理公司名称或ID、法人、注册资本、成立日期等字段的详细信息
* path oi/fundManager/2.0
* params ['name', 'pageNum', 'pageSize']


#### 投资动态


* method:  oi_investEvent
* name 投资动态
* desc 可以通过投资机构名称获取投资机构投资动态信息，包括投资产品名称、所属公司、参与轮次、投资时间、投资金额、相关新闻标题等字段的详细信息
* path oi/investEvent/2.0
* params ['name', 'pageNum', 'pageSize']


#### 统计分析


* method:  oi_stats
* name 统计分析
* desc 可以通过投资机构名称获取投资机构投资统计分析，包括月份、数量、投资规模、投资行业等
* path oi/stats/2.0
* params ['name', 'year']


#### 机构信息


* method:  pf_orgInfo
* name 机构信息
* desc 可以通过公司名称或ID获取相关私募基金信息，包括私募基金管理人名称、法定代表人/执行事务合伙人、机构类型、登记编号、成立日期等字段的相关信息
* path pf/orgInfo/2.0
* params ['id', 'name', 'keyword']


#### 会员信息


* method:  pf_member
* name 会员信息
* desc 可以通过公司名称或ID获取相关私募基金会员信息，包括是否为中国证券投资基金业协会会员、当前会员类型、入会时间等字段的相关信息
* path pf/member/2.0
* params ['id', 'name', 'keyword']


#### 法律意见书信息


* method:  pf_legalOpinion
* name 法律意见书信息
* desc 可以通过公司名称或ID获取相关私募基金法律意见书信息，包括法律意见书状态等
* path pf/legalOpinion/2.0
* params ['id', 'name', 'keyword']


#### 高管信息


* method:  pf_boss
* name 高管信息
* desc 可以通过公司名称或ID获取相关私募基金高管信息，包括法定代表人/执行事物合伙人姓名、是否有从业资格、资格取得方式等字段的相关信息
* path pf/boss/2.0
* params ['id', 'name', 'keyword']


#### 高管情况


* method:  pf_staff
* name 高管情况
* desc 可以通过公司名称或ID获取相关私募基金高管情况，包括高管姓名、是否有从业资格等字段的相关信息
* path pf/staff/2.0
* params ['id', 'name', 'keyword']


#### 产品信息


* method:  pf_product
* name 产品信息
* desc 可以通过公司名称或ID获取相关私募基金产品信息，包括暂行办法实施前/后成立的基金产品名称、基金编号等字段的相关信息
* path pf/product/2.0
* params ['id', 'name', 'keyword']


#### 诚信信息


* method:  pf_integrity
* name 诚信信息
* desc 可以通过公司名称或ID获取相关私募基金诚信信息，包括机构信息最后更新时间、特别提示信息
* path pf/integrity/2.0
* params ['id', 'name', 'keyword']


#### 建筑资质-资质资格


* method:  bq_qualification
* name 建筑资质-资质资格
* desc 可以通过公司名称或ID获取建筑资质资格信息，包括发证日期、证书有效期、资质类别、资质证书号	、资质名称、发证机关等字段的相关信息
* path bq/qualification/2.0
* params ['name', 'id', 'pageNum', 'pageSize', 'keyword']


#### 建筑资质-资质资格详情


* method:  bq_qualification_detail
* name 建筑资质-资质资格详情
* desc 可以通过建筑资质资格ID获取建筑资质资格详情，包括发证日期、证书有效期、资质类别、资质证书号  、资质名称、发证机关、证书信息等字段信息
* path bq/qualification/detail/2.0
* params ['businessId']


#### 建筑资质-注册人员


* method:  bq_regHuman
* name 建筑资质-注册人员
* desc 可以通过建筑资质注册人员ID获取建筑资质注册人员信息，包括姓名、注册类别、注册号（执业印章号）、注册专业、证书编号等字段信息
* path bq/regHuman/2.0
* params ['name', 'id', 'pageNum', 'pageSize', 'keyword']


#### 建筑资质-注册人员详情


* method:  bq_regHuman_detail
* name 建筑资质-注册人员详情
* desc 可以通过公司名称或ID获取建筑资质注册人员信息，包括姓名、注册类别、注册号（执业印章号）、注册专业、证书编号等字段的相关信息
* path bq/regHuman/detail/2.0
* params ['businessId']


#### 建筑资质-工程项目


* method:  bq_project
* name 建筑资质-工程项目
* desc 可以通过公司名称或ID获取建筑资质工程项目信息，包括项目编号、项目名称、项目属地、项目类别	、建设单位等字段的相关信息
* path bq/project/2.0
* params ['name', 'id', 'pageNum', 'pageSize', 'keyword']


#### 建筑资质-工程项目详情


* method:  bq_project_detail
* name 建筑资质-工程项目详情
* desc 可以通过建筑资质工程项目ID获取建筑资质工程项目信息，包括项目编号、项目名称、项目属地、项目类别、建设单位、招投标、合同备案、施工许可等字段信息
* path bq/project/detail/2.0
* params ['businessId', 'pageNum', 'pageSize']


#### 建筑资质-不良行为


* method:  bq_badConduct
* name 建筑资质-不良行为
* desc 可以通过公司名称或ID获取有建筑资质企业的不良行为信息，包括诚信记录编号、查看事由、实施部门（文号）、发布有效期、决定内容等字段的相关信息
* path bq/badConduct/2.0
* params ['name', 'id', 'pageNum', 'pageSize', 'keyword']


#### 搜索


* method:  search
* name 搜索
* desc 可以通过关键词获取企业列表，企业列表包括公司名称或ID、类型、成立日期、经营状态、统一社会信用代码等字段的详细信息
* path search/2.0
* params ['word']


