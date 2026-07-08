---
id: UNC@20.15.2@MMLCommand@RMV PERFNGTAIGROUP
type: MMLCommand
name: RMV PERFNGTAIGROUP（删除NG TAI组性能统计对象）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PERFNGTAIGROUP
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- AMF性能对象管理
status: active
---

# RMV PERFNGTAIGROUP（删除NG TAI组性能统计对象）

## 功能

**适用NF：AMF**

该命令用于删除指定的NG TAI组性能统计对象。

## 注意事项

- 该命令执行后立即生效。

- 在执行本命令之前请首先通过RMV NGTAIGRPMEM和RMV PERFRPTRANGE删除对本命令的NGTAIGPN参数的引用。
- 执行本命令之后，需在网管系统U2020/MAE的“拓扑”>“主拓扑”页面上，手动触发当前网元的"同步网元配置数据”，否则删除的测量对象可能会残留，导致网管系统上该测量对象对应指标上报异常，以及网管系统生成的AMF-PM规范文件中该测量对象对应指标取值缺失。未手动触发时，网管系统 “维护”>“集中任务管理”中每天定时触发“网元配置数据同步”后也可解决该残留问题，但存在时效性问题。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NGTAIGPN | NG TAI组名 | 可选必选说明：必选参数<br>参数含义：该参数用于标识基于5G TAI组的性能统计对象名称。5G TAI组内的TAI成员通过ADD NGTAIGRPMEM命令进行增加。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。不区分大小写，不支持空格及“\”且全局唯一。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PERFNGTAIGROUP]] · NG TAI组性能统计对象（PERFNGTAIGROUP）

## 使用实例

删除NG TAI组名为“huawei”的TAI组对象：

```
RMV PERFNGTAIGROUP: NGTAIGPN="huawei";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PERFNGTAIGROUP.md`
