---
id: UNC@20.15.2@MMLCommand@CLR NGTANEIBS
type: MMLCommand
name: CLR NGTANEIBS（清除TA邻接关系）
nf: UNC
version: 20.15.2
verb: CLR
object_keyword: NGTANEIBS
command_category: 动作类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N2接口管理
- TA邻接关系管理
status: active
---

# CLR NGTANEIBS（清除TA邻接关系）

## 功能

![](清除TA邻接关系（CLR NGTANEIBS）_96241938.assets/notice_3.0-zh-cn_2.png)

执行该命令，当“操作类型”选择“ALL”时将会清除所有系统自学习的TA邻接关系，可能会影响寻呼成功率。

**适用NF：AMF**

本命令用于清除系统自学习的TA邻接关系。

## 注意事项

- 该命令执行后立即生效。

- 删除邻接TA会导致无法以邻接TA为范围进行寻呼。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OPTYPE | 操作类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定清除所有还是特定TA的邻接列表。<br>数据来源：本端规划<br>取值范围：<br>- “ALL（清除所有TA邻接关系）”：清除所有TA邻接关系<br>- “SINGLE_TA（清除特定TA周围的邻接TA）”：清除特定TA周围的邻接TA<br>默认值：无<br>配置原则：无 |
| LUT | 最后更新时间(h) | 可选必选说明：必选参数<br>参数含义：该参数用于指定清除邻接TA的时间阈值：在本参数时间内未更新的邻接TA才被清除。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~720，单位是小时。当取值是0时，不检查TA邻接关系的更新时间，清除所有邻接关系。推荐值为0。<br>默认值：无<br>配置原则：无 |
| TAI | TA标识 | 可选必选说明：该参数在"OPTYPE"配置为"SINGLE_TA"时为条件必选参数。<br>参数含义：该参数用于指定中心跟踪区域的标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是11~12。TAI由MCC、MNC和TAC组成。MCC为3位十进制数字，MNC为2位或者3位十进制数字，填写时请遵循实际长度。TAC编码为十六进制数，长度固定为6位；若不足则左起用0补足6位。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGTANEIBS]] · TA邻接关系（NGTANEIBS）

## 使用实例

删除所有1小时内未更新的TA邻接关系：

```
CLR NGTANEIBS: OPTYPE=ALL, LUT=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/清除TA邻接关系（CLR-NGTANEIBS）_96241938.md`
