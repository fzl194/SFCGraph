---
id: UDG@20.15.2@MMLCommand@LOD EXTERNALDB
type: MMLCommand
name: LOD EXTERNALDB（加载外置规则数据库）
nf: UDG
version: 20.15.2
verb: LOD
object_keyword: EXTERNALDB
command_category: 动作类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务匹配策略
- 百万级业务规则库
- 外部规则数据库
status: active
---

# LOD EXTERNALDB（加载外置规则数据库）

## 功能

**适用NF：PGW-U、UPF**

该命令用于加载/升级ISU外置规则数据库，系统需要通过外部规则数据库中的规则文件进行匹配时，可以通过无损升级数据库的方式定义大规模的匹配条件。

## 注意事项

- 该命令执行后立即生效。
- 加载OTT ISU外置规则数据库后，会触发系统检查FlowFilter配置是否跟ISU外部规则数据库中的定义有冲突。冲突可以通过命令DSP COLLISIONCHECK查询。
- 数据库加载过程中会导致系统负荷过高，CPU占用率升高。
- 加载或者卸载命令两次执行间隔不能小于20秒。
- 加载完成后，使用DSP命令检查是否成功。
- 本命令会影响性能，请评估性能后配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DBTYPE | 数据库类型 | 可选必选说明：必选参数<br>参数含义：该参数用于配置外置规则库类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- OTT：OTT规则数据库。<br>默认值：无<br>配置原则：无 |
| VERSION | 外置规则数据库版本号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定外置规则数据库的版本号。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～21。长度范围是21个字符，不支持空格。版本号形式如AAAA.BB.CCCC.DDDD.EEE，ABCDE都是数字。<br>默认值：无<br>配置原则：用户规则库的版本号。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/EXTERNALDB]] · 外置规则数据库（EXTERNALDB）

## 关联任务

- [[UDG@20.15.2@Task@0-00092]]

## 使用实例

加载OTT外置规则数据库：

```
LOD EXTERNALDB: DBTYPE=OTT,VERSION="0020.02.0000.0002.001";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/加载外置规则数据库（LOD-EXTERNALDB）_94212263.md`
