---
id: UNC@20.15.2@MMLCommand@LST GTSM
type: MMLCommand
name: LST GTSM（查询GTSM全局配置属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GTSM
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP安全管理
- GTSM
status: active
---

# LST GTSM（查询GTSM全局配置属性）

## 功能

该命令用于查询GTSM全局属性。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GTSM]] · GTSM全局配置属性（GTSM）

## 使用实例

查询GTSM全局属性：

```
LST GTSM:;
```

```

        RETCODE = 0  操作成功

        结果如下
        -------------------------
        动作行为  =  通过
        (结果个数 = 1)
        ---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-GTSM.md`
