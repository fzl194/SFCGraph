---
id: UDG@20.15.2@MMLCommand@LOD PARSERDB
type: MMLCommand
name: LOD PARSERDB（加载协议解析数据库）
nf: UDG
version: 20.15.2
verb: LOD
object_keyword: PARSERDB
command_category: 动作类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 协议识别
- 特征库管理
- 解析特征库
status: active
---

# LOD PARSERDB（加载协议解析数据库）

## 功能

**适用NF：PGW-U、UPF**

该命令用来更新协议解析数据库，此过程不中断和影响业务。系统在进行协议解析时需要由协议解析数据库指定每个协议需要解析的字段。

## 注意事项

- 该命令执行后立即生效。
- 由于系统启动时，会自动加载协议解析数据库，一般情况下，不需要手工更新协议解析数据库。所以，此命令必须得到华为技术支持确认后，方可以执行，以避免协议解析数据库文件错误导致的系统异常。
- 新增协议解析数据库可以通过网管/MAE的“网元文件传输”功能或者OM Portal的“文件传输”功能进行库文件上传。
- 协议解析数据库更新需要一段时间，为保证协议解析正确，此命令在40秒内不允许再次执行，系统会自动进行检查和提示。
- 按照指定最新的解析库版本加载协议解析数据库的时候，库文件有两种来源，默认加载csp远端和本地缓存的最新库文件，如果期望加载csp远端最新的库文件，可以根据软参BYTE687进行配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOADMODE | 解析库加载模式 | 可选必选说明：必选参数<br>参数含义：该参数用于指定解析库的加载模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LATEST：指定最新的解析库版本加载。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [协议解析数据库（PARSERDB）](configobject/UDG/20.15.2/PARSERDB.md)

## 关联任务

- [[UDG@20.15.2@Task@0-00152]]

## 使用实例

运营商希望更新协议解析数据库到最新版本：

```
LOD PARSERDB:LOADMODE=LATEST;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/加载协议解析数据库（LOD-PARSERDB）_82837719.md`
