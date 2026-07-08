---
id: UNC@20.15.2@MMLCommand@SET FILEDELPOLICY
type: MMLCommand
name: SET FILEDELPOLICY（设置文件删除策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: FILEDELPOLICY
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务维护功能管理
- 操作维护
- 安全管理
- 文件删除策略
status: active
---

# SET FILEDELPOLICY（设置文件删除策略）

## 功能

该命令用于设置文件删除策略。

该命令的使用场景为：基于数据隐私安全性考虑，需要对数据进行定期清理，操作员可以使用该命令配置文件删除策略。

## 注意事项

- 系统默认文件删除策略开启，默认最大保留天数为720天。
- 文件删除策略开启后，系统会定期检测相应存盘路径下的文件，超过最大保留天数的文件会被清理掉。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| STATUS | 启用状态 | 可选必选说明：必选参数<br>参数含义：该参数用于设置文件删除策略是否启用。<br>数据来源：本端规划<br>取值范围：<br>- “DISABLE(未启用)”：表示不启用文件删除策略<br>- “ENABLE(启用)”：表示启用文件删除策略。<br>系统初始设置值：ENABLE(启用)。 |
| MAXKEEPDAYS | 最大保留天数（天） | 可选必选说明：条件必选参数<br>参数含义：该参数用于设置文件最大保留的天数。<br>数据来源：本端规划<br>取值范围：20~720<br>系统初始设置值：720。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。该参数不能取值为VNFP、ACS、VNRS_VNFC的服务实例名称。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FILEDELPOLICY]] · 文件删除策略（FILEDELPOLICY）

## 使用实例

启用文件删除策略，执行以下命令：

SET FILEDELPOLICY:STATUS=ENABLE, MAXKEEPDAYS=30 ,SERVICEINSTANCE="vnfc" ;

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置文件删除策略(SET-FILEDELPOLICY)_29626886.md`
