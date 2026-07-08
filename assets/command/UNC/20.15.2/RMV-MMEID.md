---
id: UNC@20.15.2@MMLCommand@RMV MMEID
type: MMLCommand
name: RMV MMEID（删除MMEID配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MMEID
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- MME POOL区管理
- MMEID管理
status: active
---

# RMV MMEID（删除MMEID配置）

## 功能

![](删除MMEID配置(RMV MMEID)_72225767.assets/notice_3.0-zh-cn_2.png)

删除MMEID会导致各业务功能失效。

**适用网元：MME**

该命令用于删除MMEID配置。

## 注意事项

- 该命令执行后立即生效。
- 若系统内没有MMEID，将导致如下状况：
    - 无法分配GUTI，用户附着无法接入。
    - 无法识别是否是Inter附着。
- 系统正常运行时禁止删除，否则可能会导致InterTAU成功率指标大幅下降，甚至业务中断。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定由ITU-T统一分配的移动网络所在国家的标识符。<br>取值范围：3位十进制数<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定一个国家内的PLMN标识符。<br>取值范围：位数为2或3的十进制数<br>默认值：无 |
| MMEGI | MME组识别码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MME分组的编号。<br>取值范围：4位16进制编码。<br>默认值：无<br>说明：- MME组识别码在同一个PLMN下是唯一的。<br>- 可能会有多个PLMN同用一个MME组识别码。<br>- 同一个MME不能属于多个MME组。 |
| MMEC | MME编码（起始值） | 可选必选说明：必选参数<br>参数含义：该参数用于指定MME组内的MME编码（起始值）。<br>取值范围：2位16进制编码。<br>默认值：无<br>说明：- 一个MME组内MME编码必须唯一。<br>- MME编码在互相覆盖的所有MME组中必须唯一。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MMEID]] · MMEID配置（MMEID）

## 使用实例

删除一个 “移动国家码” 为 “123” 、 “移动网号” 为 “01” 、 “MME组识别码” 为 “8002” 、 “MME编码（起始值）” 为 “01” 的MME节点：

RMV MMEID: MCC="123",MNC="01", MMEGI="8002",MMEC="01";

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-MMEID.md`
