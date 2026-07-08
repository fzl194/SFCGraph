---
id: UDG@20.15.2@MMLCommand@CLR AFMATCHSTATIC
type: MMLCommand
name: CLR AFMATCHSTATIC（清零欺诈场景的匹配统计计数）
nf: UDG
version: 20.15.2
verb: CLR
object_keyword: AFMATCHSTATIC
command_category: 动作类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务防欺诈
- HTTP欺诈场景的匹配情况统计
status: active
---

# CLR AFMATCHSTATIC（清零欺诈场景的匹配统计计数）

## 功能

**适用NF：PGW-U、UPF**

命令用于清零欺诈场景的匹配统计计数。HTTP防欺诈功能开启后，欺诈场景匹配统计计数会一直进行统计，可以使用本命令清除之前的计数，便于观察特定时间段内计数的变化情况。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AFMATCHTYPE | 欺诈场景类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定欺诈场景类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- AF_DATABASE：防欺诈库定义的欺诈场景。<br>- AF_SOFTWARE：软参定义的欺诈场景。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/AFMATCHSTATIC]] · HTTP欺诈场景的统计结果（AFMATCHSTATIC）

## 使用实例

清零软参欺诈场景匹配统计计数：

```
CLR AFMATCHSTATIC:AFMATCHTYPE=AF_SOFTWARE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/CLR-AFMATCHSTATIC.md`
