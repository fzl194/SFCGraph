# 修改DNAI粒度的UPF选择策略（MOD DNAIUPSELPLY）

- [命令功能](#ZH-CN_MMLREF_0000001318357781__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001318357781__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001318357781__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001318357781__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001318357781)

**适用NF：PGW-C、SMF**

该命令用于修改DNAI粒度的UPF选择策略。

## [注意事项](#ZH-CN_MMLREF_0000001318357781)

该命令执行后立即生效。

#### [操作用户权限](#ZH-CN_MMLREF_0000001318357781)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001318357781)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNAI | 数据网络访问标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定数据网络访问标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| SHAREDPRIFLAG | 分流场景下共享UPF优选开关 | 可选必选说明：可选参数<br>参数含义：该参数用于该DNAI下SMF在分流场景下是否优选共享UPF。该优选策略属于合一优先选择，生效顺位与合一优先选择相同。<br>数据来源：本端规划<br>取值范围：<br>- “INHERIT（继承）”：继承当前APN的分流场景下共享UPF优选开关（APNUPSELPLY:SHAREDPRIFLAG）。<br>- “DISABLE（关）”：分流场景下优选共享UPF不生效。<br>- “ENABLE（开）”：分流场景下优选共享UPF。<br>默认值：无<br>配置原则：无 |
| PRIORITYFLAG | 基于优先级优选UPF开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指示该DNAI下SMF基于优先级选择UPF的功能是否开启。<br>数据来源：本端规划<br>取值范围：<br>- “INHERIT（继承）”：继承APN级的优先级选择开关。<br>- “DISABLE（关）”：关闭基于优先级选择UPF功能。<br>- “ENABLE（开）”：打开基于优先级选择UPF功能。<br>默认值：无<br>配置原则：<br>- 可以使用不同粒度的配置打开基于优先级选择UPF的功能（UPSELECTFLAG:PRIORITYFLAG、APNUPSELPLY:PRIORITYFLAG、DNAIUPSELPLY:PRIORITYFLAG）。<br>- 如果要使优先级优选容许过载UPF开关（UPSELECTFLAG:OVERLOADALWFLAG）、合一与优先级优选策略（APNUPSELPLY:COMBINEPRISTG）、选择合一UPF的优先级策略（APNUPSELPLY:COMBINEDSELSTG）生效，需要打开基于优先级选择UPF的功能。<br>- 基于PNFPROFILE、PNFDNN、PNFTAI、PNFTAIRANGE、PNFSMFSERAREA、PNFDNAI的UPF优先级需要在打开基于优先级选择UPF的功能后才生效。<br>- 基于PNFDNN、PNFTAI、PNFTAIRANGE、PNFSMFSERAREA、PNFDNAI的UPF特定容量需要在打开基于优先级选择UPF的功能后才生效。 |
| LOADFLTFLAG | 基于负载优选UPF开关 | 可选必选说明：可选参数<br>参数含义：该参数用于指示该DNAI下SMF是否打开基于UPF负载信息进行UPF优选的功能。<br>数据来源：本端规划<br>取值范围：<br>- “INHERIT（继承）”：继承整机的基于负载优选UPF开关（UPSELECTFLAG:LOADFLTFLAG）。<br>- “DISABLE（关）”：关闭基于负载选择UPF功能。<br>- “ENABLE（开）”：打开基于负载选择UPF功能。<br>默认值：无<br>配置原则：无 |

## [使用实例](#ZH-CN_MMLREF_0000001318357781)

- 修改SMF在DNAI下在分流场景优选共享UPF，DNAI名称为huawei.com。
  ```
  MOD DNAIUPSELPLY: DNAI="huawei.com",SHAREDPRIFLAG=ENABLE;
  ```
- 修改SMF在DNAI下在支持基于优先级优选UPF，DNAI名称为huawei.com。
  ```
  MOD DNAIUPSELPLY: DNAI="huawei.com",PRIORITYFLAG=ENABLE;
  ```
- 修改SMF在DNAI下在支持基于负载优选UPF，DNAI名称为huawei.com。
  ```
  MOD DNAIUPSELPLY: DNAI="huawei.com",LOADFLTFLAG=ENABLE;
  ```
