---
id: UNC@20.15.2@MMLCommand@LST GLBEDRXATTR
type: MMLCommand
name: LST GLBEDRXATTR（查询全局终端接入eDRX模式属性）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GLBEDRXATTR
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- eDRX模式管理
status: active
---

# LST GLBEDRXATTR（查询全局终端接入eDRX模式属性）

## 功能

**适用NF：SMF**

该命令用于查询全局终端接入的eDRX模式。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [全局终端接入eDRX模式属性（GLBEDRXATTR）](configobject/UNC/20.15.2/GLBEDRXATTR.md)

## 使用实例

假如用户需要对全局终端接入的eDRX模式进行查询，则使用该实例：

```
%%LST GLBEDRXATTR:;%%
RETCODE = 0  操作成功

结果如下
------------------------
              支持eDRX模式开关  =  使能
        下行包缓存数获取优先级  =  从DLBUFFPKTCNT获取
                  下行包缓存数  =  10
            下行包缓存额外时长  =  10
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询全局终端接入eDRX模式属性（LST-GLBEDRXATTR）_82861629.md`
