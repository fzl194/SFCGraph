---
id: UNC@20.15.2@MMLCommand@DSP PFCPSESSIONINFO
type: MMLCommand
name: DSP PFCPSESSIONINFO（显示PFCP会话信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PFCPSESSIONINFO
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- PFCP路径管理
- PFCP会话信息查询
status: active
---

# DSP PFCPSESSIONINFO（显示PFCP会话信息）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于显示PFCP的会话信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DSPINFOTYPE | 信息呈现方式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定信息呈现方式。<br>数据来源：本端规划<br>取值范围：<br>- SIMPLE（简约信息呈现）<br>- DETAILED（详细信息呈现）<br>默认值：无<br>配置原则：无 |
| QUERYTYPE | 查询方式 | 可选必选说明：该参数在"DSPINFOTYPE"配置为"SIMPLE"时为条件必选参数。<br>参数含义：该参数用于指定查询方式。<br>数据来源：本端规划<br>取值范围：<br>- IMSI（用户IMSI号）<br>默认值：IMSI<br>配置原则：无 |
| IMSI | IMSI | 可选必选说明：该参数在"DSPINFOTYPE"配置为"SIMPLE"时为条件必选参数。<br>参数含义：该参数用于指定用户永久标识或者国际移动用户标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~15。<br>默认值：无<br>配置原则：无 |
| DETAILTYPE | 详单类型 | 可选必选说明：该参数在"DSPINFOTYPE"配置为"DETAILED"时为条件必选参数。<br>参数含义：该参数用于指定显示的详单类型。<br>数据来源：本端规划<br>取值范围：<br>- PDR（PDR）<br>- FAR（FAR）<br>- BAR（BAR）<br>- UPCURR（UPC创建的URR）<br>- QER（QER）<br>- TUNNEL（Tunnel）<br>- PFCPSESSION（PFCP会话）<br>默认值：PFCPSESSION<br>配置原则：无 |
| CPSEID | CP的Seid | 可选必选说明：该参数在"DETAILTYPE"配置为"PFCPSESSION"、"PDR"、"FAR"、"QER"、"BAR"、"UPCURR"、"TUNNEL"时为条件必选参数。<br>参数含义：该参数用于指定CP的Seid。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~9223372036854775807。<br>默认值：无<br>配置原则：无 |
| PDRID | PDR标识 | 可选必选说明：该参数在"DETAILTYPE"配置为"PDR"时为条件可选参数。<br>参数含义：该参数用于显示PDR标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| FARID | FAR标识 | 可选必选说明：该参数在"DETAILTYPE"配置为"FAR"时为条件可选参数。<br>参数含义：该参数用于显示FAR标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| QERID | QER标识 | 可选必选说明：该参数在"DETAILTYPE"配置为"QER"时为条件可选参数。<br>参数含义：该参数用于显示QER标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| URRID | URR标识 | 可选必选说明：该参数在"DETAILTYPE"配置为"UPCURR"时为条件可选参数。<br>参数含义：该参数用于显示URR标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |
| BEARERNO | Bearer标识 | 可选必选说明：该参数在"DETAILTYPE"配置为"PDR"、"FAR"、"QER"、"UPCURR"、"TUNNEL"时为条件可选参数。<br>参数含义：该参数用于显示Bearer标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| BARID | BAR标识 | 可选必选说明：该参数在"DETAILTYPE"配置为"BAR"时为条件可选参数。<br>参数含义：该参数用于显示BAR标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| QFI | QFI | 可选必选说明：该参数在"DETAILTYPE"配置为"PDR"、"FAR"、"QER"、"UPCURR"时为条件可选参数。<br>参数含义：该参数用于显示QFI。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| PCCRULEID | PCC Rule标识 | 可选必选说明：该参数在"DETAILTYPE"配置为"PDR"、"FAR"、"QER"时为条件可选参数。<br>参数含义：该参数用于显示PCC Rule标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PFCPSESSIONINFO]] · PFCP会话信息（PFCPSESSIONINFO）

## 使用实例

- 查询类型为IMSI，查询方式为简单查询，IMSI为123035000100001：
  ```
  %%DSP PFCPSESSIONINFO: DSPINFOTYPE=SIMPLE, QUERYTYPE=IMSI, IMSI="123032111110001";%%
  RETCODE = 0  操作成功

  Pfcpsession Info
  ----------------
                   IMSI  =  123035000100001
            PDU会话标识  =  5
        链接的EPS承载ID  =  0
               CP的Seid  =  8070591282084708358
                 UP角色  =  Access|MainAnchor|5g|BySmfN11
             UP实例标识  =  upf_instance_1
           PFCP会话状态  =  正常
  (结果个数 = 1)

  ---    END
  ```
- 查询类型为TUNNEL，查询方式为详细查询，CPSEID为8070591282084708358的PFCP会话信息，CPSEID可使用本命令的简单查询获得：
  ```
  %%DSP PFCPSESSIONINFO: DSPINFOTYPE=DETAILED, DETAILTYPE=TUNNEL, CPSEID=8070591282084708358;%%
  RETCODE = 0  操作成功

  Pfcpsession Info
  ----------------
  Bearer标识     隧道类型    隧道TEID       IPv4地址       IPv6地址    

  0              1            10           0.0.0.0       2001:db8:0:1:1:1:1:1
  0              2            2            10.0.0.1      ::                  
  0              28           2154692610   10.0.1.1      ::                  
  0              29           11           10.0.2.1      ::                  
  (Number of results = 4)

  ---    END
  ```
- 查询类型为PDR，查询方式为详细查询，CPSEID为8070591282084708358的PFCP会话信息，CPSEID可使用本命令的简单查询获得：
  ```
  %%DSP PFCPSESSIONINFO: DSPINFOTYPE=DETAILED, DETAILTYPE=PDR, CPSEID=8070591282084708358;%%
  RETCODE = 0  操作成功

  Pfcpsession Info
  ----------------
  PDR标识   本端接口类型     PDR类型   PDR优先级     PDR方向                  PCC Rule标识  Bearer标识   QFI   关联的FAR标识   关联的URR列表   关联的QER列表          是否IMS信令  关联的APP标识  

  1025      UpIfTypeN3Upf    1         4294967295    Bidirectional Uplink     65535         0            0     540016641       NULL            1895825408             FALSE        NULL           
  2050      UpIfTypeN9c      2         4294967295    Bidirectional Downlink   65535         0            0     541065218       NULL            1895825408             FALSE        NULL           
  9219      UpIfTypeN3Upf    9         0             Unidirectional Uplink    65535         2            2     547356675       NULL            1929379842             FALSE        NULL           
  10244     UpIfTypeN9c      10        0             Unidirectional Downlink  65535         2            2     548405252       NULL            1929379842             FALSE        NULL           
  9221      UpIfTypeN3Upf    9         0             Unidirectional Uplink    65535         1            1     547356677       NULL            1929379841 1895825408  FALSE        NULL           
  10246     UpIfTypeN9c      10        0             Unidirectional Downlink  65535         1            1     548405254       NULL            1929379841 1895825408  FALSE        NULL           
  (Number of results = 6)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PFCPSESSIONINFO.md`
