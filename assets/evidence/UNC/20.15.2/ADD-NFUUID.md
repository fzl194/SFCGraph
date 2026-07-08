# 增加NF UUID信息（ADD NFUUID）

- [命令功能](#ZH-CN_MMLREF_0209652589__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0209652589__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0209652589__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0209652589__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0209652589)

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG、CBCF、SPF**

该命令用于为NF实例生成NF实例标识。NF实例标识为UUID（通用唯一标识符，Universally Unique Identifier）。在NF向NRF发起注册/更新/去注册等流程中，均会携带UUID，用于唯一标识NF实例。

## [注意事项](#ZH-CN_MMLREF_0209652589)

- 该命令执行后立即生效。

- NF实例标识NFINSTANCEID参数推荐免填写，直接由系统自动生成。如果手工填写了该参数且符合格式要求，以手工填写为准。
- 对于已经存在的NF实例，若要修改其NF实例标识，则必须在修改后通过RMV SBIAPLE和ADD SBIAPLE命令删除并重建链路集。重建链路集会导致所有链路短暂中断。

- 最多可输入23条记录。

#### [操作用户权限](#ZH-CN_MMLREF_0209652589)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0209652589)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | NF类型 | 可选必选说明：必选参数<br>参数含义：本参数用于指定NF类型。<br>数据来源：全网规划<br>取值范围：<br>- NfInvalid（NfInvalid）<br>- NfNRF（NfNRF）<br>- NfUDM（NfUDM）<br>- NfAMF（NfAMF）<br>- NfSMF（NfSMF）<br>- NfAUSF（NfAUSF）<br>- NfNEF（NfNEF）<br>- NfPCF（NfPCF）<br>- NfSMSF（NfSMSF）<br>- NfNSSF（NfNSSF）<br>- NfUDR（NfUDR）<br>- NfLMF（NfLMF）<br>- NfGMLC（NfGMLC）<br>- Nf5G_EIR（Nf5G_EIR）<br>- NfSEPP（NfSEPP）<br>- NfUPF（NfUPF）<br>- NfN3IWF（NfN3IWF）<br>- NfAF（NfAF）<br>- NfUDSF（NfUDSF）<br>- NfBSF（NfBSF）<br>- NfCHF（NfCHF）<br>- NfNWDAF（NfNWDAF）<br>- “NfTypeMAX（NfTypeMAX）”：已废弃。<br>- NfMBSMF（NfMBSMF）<br>- NfCBCF（NfCBCF）<br>- NfSCF（NfSCF）<br>- NfSPF（NfSPF）<br>默认值：无<br>配置原则：<br>仅可以选择网元支持的NF实例。 |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：必选参数<br>参数含义：本参数用于指定NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>本参数的构成字符只能是字母A～Z或a～z、数字0～9、中划线"-"和下划线"_"，例如，AMF_Instance_0。 |
| NFINSTANCEID | NF实例标识 | 可选必选说明：可选参数<br>参数含义：本参数用于指定NF实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~36。该参数大小写不敏感。<br>默认值：无<br>配置原则：<br>- 如果该参数用户未填写，则系统会在后台自动生成NF实例标识UUID。推荐不填写，由系统自动生成。<br>- 在系统重装并希望保持系统原有UUID不变的情况下，可以手动填写为系统原有UUID。UUID手动填写要求的格式为32个BCD（Binary-Coded Decimal‎）码，不包含连字号。即以连字号分为五段，形式为8-4-4-4-12的16进制的32位字符串。例如，00000000-0000-0000-c000-000000000046。<br>- UUID的最后12位为NodeID，支持自定义输入，即只须输入最后12位即可，其它位的字符还是由系统自动生成。 |

## [使用实例](#ZH-CN_MMLREF_0209652589)

- 场景一，运营商A需要系统自动生成UUID。其中NF类型为NfAMF，NF实例名称为AMF_Instance_0。
  ```
  ADD NFUUID: NFTYPE=NfAMF, NFINSTANCENAME="AMF_Instance_0";
  ```
- 场景二，运营商A需要自定义UUID的NodeID，其中NF类型为NfAMF，NF实例名称为AMF_Instance_0，NodeID为030101000001。
  ```
  ADD NFUUID: NFTYPE=NfAMF, NFINSTANCENAME="AMF_Instance_0",NFINSTANCEID="030101000001";
  ```
- 场景三，运营商A的设备重新实例化，需要导入实例化前的配置，其中NF类型为NfAMF，NF实例名称为AMF_Instance_0，NF实例标识为bdc3f6f6-69ac-4c06-bfe5-030101000001。
  ```
  ADD NFUUID: NFTYPE=NfAMF, NFINSTANCENAME="AMF_Instance_0",NFINSTANCEID="bdc3f6f6-69ac-4c06-bfe5-030101000001";
  ```
