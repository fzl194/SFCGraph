# 查询PIM表项下游信息（DSP PIMROUTEDW）

- [命令功能](#ZH-CN_CONCEPT_0000001550121610__1.3.1.1)
- [注意事项](#ZH-CN_CONCEPT_0000001550121610__1.3.2.1)
- [操作用户权限](#ZH-CN_CONCEPT_0000001550121610__1.3.3.1)
- [参数说明](#ZH-CN_CONCEPT_0000001550121610__1.3.4.1)
- [使用实例](#ZH-CN_CONCEPT_0000001550121610__1.3.5.1)
- [输出结果说明](#ZH-CN_CONCEPT_0000001550121610__1.3.6.1)

#### [命令功能](#ZH-CN_CONCEPT_0000001550121610)

该命令用于显示PIM表项下游信息。

#### [注意事项](#ZH-CN_CONCEPT_0000001550121610)

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### [操作用户权限](#ZH-CN_CONCEPT_0000001550121610)

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

#### [参数说明](#ZH-CN_CONCEPT_0000001550121610)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ADDRESSFAMILY | 地址族 | 可选必选说明：必选参数<br>参数含义：该参数用于表示地址族类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ipv4unicast：IPv4单播。<br>默认值：无 |
| MASTERSLAVETYPE | OMU类型 | 可选必选说明：可选参数<br>参数含义：该参数表示OMU类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MASTER：主。<br>- SLAVE：备。<br>默认值：MASTER |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：_public_<br>配置原则：通过LST L3VPNINST查看当前已存在的VPN实例。 |
| SRCADDR | 源地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSFAMILY”配置为“ipv4unicast”时为必选参数。<br>参数含义：该参数用于表示源地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| GRPADDR | 组地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ADDRESSFAMILY”配置为“ipv4unicast”时为必选参数。<br>参数含义：该参数用于表示组地址。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |
| SGDSOIFNAME | 出接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示出接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

#### [使用实例](#ZH-CN_CONCEPT_0000001550121610)

显示PIM表项下游信息：

```
DSP PIMROUTEDW:VRFNAME="_public_",ADDRESSFAMILY=ipv4unicast,SRCADDR="10.1.1.2",GRPADDR="239.0.0.1",SGDSOIFNAME="Ethernet64/0/3";
```

```
RETCODE = 0  操作成功。

结果如下
--------
                  VPN实例名称  =  _public_
                       地址族  =  IPv4单播
                       源地址  =  10.1.1.2
                       组地址  =  239.0.0.1
                   出接口名称  =  Ethernet64/0/3
                 下游协议类型  =  static
           下游接口已存在时间  =  00:09:34
             下游接口超时时间  =  00:00:00
               下游接口DR状态  =  TRUE
                     下游状态  =  无状态
          下游接口PPT超时时间  =  00:00:00
                 assert状态机  =  无状态
           下游assert超时时间  =  00:00:00
            assert winner地址  =  0.0.0.0
         assert winner Metric  =  0
   assert winner Metric优先级  =  0
             是否有本地接收者  =  TRUE
                  下游RPT状态  =  无状态
          下游RPT PPT超时时间  =  00:00:00
              下游RPT超时时间  =  00:00:00
(结果个数 = 1)
---    END
```

#### [输出结果说明](#ZH-CN_CONCEPT_0000001550121610)

| 输出项名称 | 输出项解释 |
| --- | --- |
| VPN实例名称 | 用于表示VPN实例名称。 |
| 地址族 | 用于表示地址族类型。 |
| 源地址 | 用于表示源地址。 |
| 组地址 | 用于表示组地址。 |
| 出接口名称 | 用于表示出接口名称。 |
| 下游协议类型 | 用于表示下游协议类型。 |
| 下游接口已存在时间 | 用于表示下游接口已存在时间。 |
| 下游接口超时时间 | 用于表示下游接口超时时间。 |
| 下游接口DR状态 | 用于表示下游接口DR状态。 |
| 下游状态 | 用于表示下游状态，包括：<br>- 无状态。<br>- 剪枝延迟状态。<br>- 加入状态。<br>- 剪枝状态。 |
| 下游接口PPT超时时间 | 用于表示下游接口PPT超时时间。 |
| assert状态机 | 用于表示assert状态机，包括：<br>- 无状态。<br>- Winner状态。<br>- Loser状态。 |
| 下游assert超时时间 | 用于表示下游assert超时时间。 |
| assert winner地址 | 用于表示assert winner地址。 |
| assert winner Metric | 用于表示assert winner Metric。 |
| assert winner Metric优先级 | 用于表示assert winner Metric优先级。 |
| 是否有本地接收者 | 用于表示是否有本地接收者。 |
| 下游RPT状态 | 用于表示下游RPT状态，包括：<br>- 无状态。<br>- 剪枝状态。<br>- 剪枝延迟状态。<br>- 非法值。 |
| 下游RPT PPT超时时间 | 用于表示下游RPT PPT超时时间。 |
| 下游RPT超时时间 | 用于表示下游RPT超时时间。 |
