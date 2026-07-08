---
id: UNC@20.15.2@MMLCommand@RMV NGALGPRIORITY
type: MMLCommand
name: RMV NGALGPRIORITY（删除5G算法优先级属性）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGALGPRIORITY
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 业务安全管理
- 安全算法优先级管理
status: active
---

# RMV NGALGPRIORITY（删除5G算法优先级属性）

## 功能

![](删除5G算法优先级属性（RMV NGALGPRIORITY）_09652634.assets/notice_3.0-zh-cn_2.png)

执行该命令可能导致加密算法或者完整性算法生效变化，导致终端接入异常。

**适用NF：AMF**

该命令用于删除指定加密或完整性算法的优先级属性。

## 注意事项

- 该命令执行后立即生效。

- 删除某种算法优先级属性后，如果AMF还配有其它算法的优先级属性，则以其它算法中优先级最高的算法为准；如果所有算法均未设置优先级属性，系统会根据算法的默认优先级属性（从高到低分别为AES、SNOW 3G、ZUC、空加密算法）和UE进行协商，最终确定采用的加密或完整性算法。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALGTYPE | 算法类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对何种类型的算法设置优先级属性，分加解密算法和完整性算法两种类型。<br>数据来源：全网规划<br>取值范围：<br>- “CIPH（加密算法）”：加密算法<br>- “INTE（完整性算法）”：完整性算法<br>默认值：无<br>配置原则：无 |
| ALGCIPH | 加密算法 | 可选必选说明：该参数在"ALGTYPE"配置为"CIPH"时为条件必选参数。<br>参数含义：该参数用于指定对何种加密算法设置优先级属性。<br>数据来源：全网规划<br>取值范围：<br>- “NEA0（空加密算法）”：空加密算法<br>- “NEA1（SNOW 3G加密算法）”：SNOW 3G加密算法<br>- “NEA2（AES加密算法）”：AES加密算法<br>- “NEA3（ZUC加密算法）”：ZUC加密算法<br>默认值：无<br>配置原则：无 |
| ALGINTE | 完整性算法 | 可选必选说明：该参数在"ALGTYPE"配置为"INTE"时为条件必选参数。<br>参数含义：该参数用于指定对何种完整性算法设置优先级属性。<br>数据来源：本端规划<br>取值范围：<br>- “NIA1（SNOW 3G完整性算法）”：SNOW 3G完整性算法<br>- “NIA2（AES完整性算法）”：AES完整性算法<br>- “NIA3（ZUC完整性算法）”：ZUC完整性算法<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NGALGPRIORITY]] · 5G算法优先级属性（NGALGPRIORITY）

## 使用实例

删除算法类型为NEA1（SNOW 3G）加密算法的优先级属性配置信息，执行如下命令：

```
RMV NGALGPRIORITY: ALGTYPE=CIPH, ALGCIPH=NEA1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NGALGPRIORITY.md`
