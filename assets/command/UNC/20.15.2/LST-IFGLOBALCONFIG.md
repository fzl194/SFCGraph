---
id: UNC@20.15.2@MMLCommand@LST IFGLOBALCONFIG
type: MMLCommand
name: LST IFGLOBALCONFIG（查询接口全局配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: IFGLOBALCONFIG
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 接口管理
- 接口全局配置
status: active
---

# LST IFGLOBALCONFIG（查询接口全局配置）

## 功能

该命令用于显示接口全局属性。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@IFGLOBALCONFIG]] · 接口全局配置（IFGLOBALCONFIG）

## 使用实例

查询全局的流量统计间隔和接口首次Down告警上报的使能状态：

```
LST IFGLOBALCONFIG:;
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
   全局流量统计间隔（s） = 5
使能接口首次Down告警上报 = FALSE
(结果个数 = 1)
---   END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-IFGLOBALCONFIG.md`
