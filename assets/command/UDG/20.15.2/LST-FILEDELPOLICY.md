---
id: UDG@20.15.2@MMLCommand@LST FILEDELPOLICY
type: MMLCommand
name: LST FILEDELPOLICY（查询文件删除策略）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: FILEDELPOLICY
command_category: 查询类
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

# LST FILEDELPOLICY（查询文件删除策略）

## 功能

该命令用于查询文件删除策略。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。该参数不能取值为VNFP、ACS、VNRS_VNFC的服务实例名称。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FILEDELPOLICY]] · 文件删除策略（FILEDELPOLICY）

## 使用实例

查询文件删除策略，执行以下命令：

LST FILEDELPOLICY: SERVICEINSTANCE="vnfc" ;

```
RETCODE = 0  操作成功。

结果如下
--------
          启用状态  =  启用
最大保留天数（天）  =  30
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询文件删除策略(LST-FILEDELPOLICY)_29626887.md`
