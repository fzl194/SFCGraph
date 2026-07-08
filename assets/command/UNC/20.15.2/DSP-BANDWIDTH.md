---
id: UNC@20.15.2@MMLCommand@DSP BANDWIDTH
type: MMLCommand
name: DSP BANDWIDTH（显示带宽配置及使用情况）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: BANDWIDTH
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- QoS映射
- 显示带宽配置及使用情况
status: active
---

# DSP BANDWIDTH（显示带宽配置及使用情况）

## 功能

**适用NF：SGW-C、PGW-C、GGSN**

该命令用于查看带宽配置及使用状况。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APN | APN | 可选必选说明：必选参数<br>参数含义：该参数用于指定APN名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/BANDWIDTH]] · 带宽配置及使用情况（BANDWIDTH）

## 使用实例

当希望查询当前带宽配置及使用状况时，使用如下命令：

```
%%DSP BANDWIDTH: APN="1";%%
RETCODE = 0  操作成功。

基于接入点的频带控制
-------------------------
          APN最大 PDP 上下文数 = 0
      APN当前 PDP 上下文编号 = 0
             APN最大带宽（千比特/秒）= 0
     APN当前 PDP 带宽（千比特/秒） = 0
APN当前剩余 PDP 带宽（千比特/秒）= 0
（结果数 = 1）
---完
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示带宽配置及使用情况（DSP-BANDWIDTH）_28213689.md`
