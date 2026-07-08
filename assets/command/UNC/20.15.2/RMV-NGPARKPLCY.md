---
id: UNC@20.15.2@MMLCommand@RMV NGPARKPLCY
type: MMLCommand
name: RMV NGPARKPLCY（删除园区策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NGPARKPLCY
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 园区策略管理
status: active
---

# RMV NGPARKPLCY（删除园区策略）

## 功能

**适用NF：AMF**

该命令用于删除园区策略。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PARKID | 园区标识 | 可选必选说明：必选参数<br>参数含义：该参数用于标识一个园区。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [园区策略（NGPARKPLCY）](configobject/UNC/20.15.2/NGPARKPLCY.md)

## 使用实例

删除园区标识为“park”的园区策略，执行如下命令：

```
RMV NGPARKPLCY: PARKID="park";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除园区策略（RMV-NGPARKPLCY）_06399926.md`
