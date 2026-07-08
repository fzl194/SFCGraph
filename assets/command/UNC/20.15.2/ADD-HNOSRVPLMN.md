---
id: UNC@20.15.2@MMLCommand@ADD HNOSRVPLMN
type: MMLCommand
name: ADD HNOSRVPLMN（增加归属网络Serving PLMN信息）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: HNOSRVPLMN
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
max_records: 256
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 归属网络运营商管理
- 归属网络Serving PLMN管理
status: active
---

# ADD HNOSRVPLMN（增加归属网络Serving PLMN信息）

## 功能

**适用网元：SGSN**

在MOCN、GWCN下，当一个运营商有多个HPLMN时，可以通过此命令为当前运营商的Non-supporting UE提供一个或多个Serving PLMN。

在MOCN、GWCN下，当一个运营商有多个HPLMN时，运营商通常对外只使用一个PLMN ID，这样使在用户呈现上和网间计费结算上更为简洁，因此一般只为一个运营商配置一个Serving PLMN。

## 注意事项

- 此命令的最大记录数为256。
- 此命令执行后立即生效。
- 若MCC相同，有效长度为2的MNC和3位的MNC前两位不允许相同。
- 在MOCN、GWCN下，当在一个运营商中为Non-supporting UE配置多个Serving PLMN时，则优先基于UE的IMSI匹配Serving PLMN，如果匹配上，选择此Serving PLMN；如果没有匹配上，将随机选择此运营商下的Serving PLMN。
- 在MOCN、GWCN下，当一个运营商有多个HPLMN时，如果没有通过此配置命令为Non-supporting UE指定一个Serving PLMN，则系统随机的从多个HPLMN中为此用户选择一个作为Serving PLMN。
- 对于MOCN，需要先将[**SET CHGCDR**](../../../../计费管理/计费控制/设置计费CDR参数（SET CHGCDR）_26145372.md)中的“Non-supporting UE的PLMN获取策略”设置为“SRV_PLMN(SERVING PLMN)”后，此配置的数据才会生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NOID | 运营商标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定运营商标识。<br>数据来源：整网规划<br>取值范围：0～64，128～254<br>默认值：无<br>配置原则：<br>- 此参数需要先在[**ADD HPLMN**](../MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md)或[**ADD MVNONET**](../MVNO管理/MVNO网络标识配置表/增加MVNO网络配置信息(ADD MVNONET)_72345663.md)中先配置好。 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定该运营商的Serving PLMN的移动国家号码。<br>数据来源：整网规划<br>取值范围：3位十进制数字<br>默认值：无<br>配置原则：<br>- 此参数需要先在[**ADD HPLMN**](../MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md)或[**ADD MVNONET**](../MVNO管理/MVNO网络标识配置表/增加MVNO网络配置信息(ADD MVNONET)_72345663.md)中先配置好。 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定该运营商的Serving PLMN的移动网号码。<br>数据来源：整网规划<br>取值范围：位数为2或3的十进制数字<br>默认值：无<br>配置原则：<br>- 此参数需要先在[**ADD HPLMN**](../MNO管理/MNO网络配置表/增加本地PLMN(ADD HPLMN)_26146074.md)或[**ADD MVNONET**](../MVNO管理/MVNO网络标识配置表/增加MVNO网络配置信息(ADD MVNONET)_72345663.md)中先配置好。 |
| PLMNN | 运营商名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定运营商名称。<br>数据来源：整网规划<br>取值范围：0~50位字符串<br>默认值：noname |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HNOSRVPLMN]] · 归属网络Serving PLMN信息（HNOSRVPLMN）

## 使用实例

增加一个HNPSRVPLMN配置：运营商标识为0，移动国家码为123，移动网号为03，运营商名称为AAA

ADD HNOSRVPLMN: NOID=0, MCC="123", MNC="03", PLMNN="AAA";

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-HNOSRVPLMN.md`
