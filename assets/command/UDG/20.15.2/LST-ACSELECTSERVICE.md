---
id: UDG@20.15.2@MMLCommand@LST ACSELECTSERVICE
type: MMLCommand
name: LST ACSELECTSERVICE（查询仲裁服务配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: ACSELECTSERVICE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 系统维护
- 仲裁服务配置
status: active
---

# LST ACSELECTSERVICE（查询仲裁服务配置）

## 功能

该命令用于查询ETCD仲裁服务的客户端相关配置，包括ETCD仲裁的开关和ETCD灯塔特性的开关

本命令只适用于ACS服务，其他微服务请使用LST ELECTSERVICE命令。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

无。

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@ACSELECTSERVICE]] · 仲裁服务状态（ACSELECTSERVICE）

## 使用实例

查询仲裁服务打开/关闭配置：

```
LST ACSELECTSERVICE:;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
       仲裁服务开关配置 =  使能
       ETCD灯塔开关配置 =  使能
(结果个数 = 1)
 ---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-ACSELECTSERVICE.md`
