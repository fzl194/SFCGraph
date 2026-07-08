---
id: UNC@20.15.2@MMLCommand@DSP NGLANUPINFO
type: MMLCommand
name: DSP NGLANUPINFO（显示5G LAN UE会话分布情况）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NGLANUPINFO
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 5G LAN管理
- 查询5G LAN UE会话分布信息
status: active
---

# DSP NGLANUPINFO（显示5G LAN UE会话分布情况）

## 功能

**适用NF：SMF**

该命令用于查询SMF上5G LAN UE会话在每个UPF上的分布情况。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGLANUPINFOTYPE | 查询分类 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询分类。<br>数据来源：本端规划<br>取值范围：<br>- “ALL（查询所有信息）”：查询所有UE会话在每个UPF上的分布情况<br>- “NGLANGROUPID（5G LAN组ID）”：查询指定GRUOPID中的UE会话分布情况<br>- “UPINSTANCEID（UPF实例名称）”：查询指定UPF中的UE会话分布情况<br>默认值：ALL<br>配置原则：无 |
| NGLANGROUPID | 5G LAN组ID | 可选必选说明：该参数在"NGLANUPINFOTYPE"配置为"NGLANGROUPID"时为条件必选参数。<br>参数含义：该参数用于指定5G LAN群组的ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是18~37。字母大小写不敏感且全局唯一。<br>默认值：无<br>配置原则：<br>NGLANGROUPID以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A-F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A-F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。 |
| UPFINSTANCEID | UPF实例名称 | 可选必选说明：该参数在"NGLANUPINFOTYPE"配置为"UPINSTANCEID"时为条件必选参数。<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NGLANUPINFO]] · 5G LAN UE会话分布情况（NGLANUPINFO）

## 使用实例

当希望查询整系统的UE会话在每个UPF上的分布情况时，使用如下命令：

```
%%DSP NGLANUPINFO: NGLANUPINFOTYPE=ALL;%%
RETCODE = 0  操作成功

            结果如下
------------------------
5G LAN组ID       UPF实例名称   UE会话数  惯性运行状态

a0000001-460-03-01  upf_instance_3  1    非惯性运行状态
a0000001-460-03-02  upf_instance_3  1    非惯性运行状态
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NGLANUPINFO.md`
