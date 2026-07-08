---
id: UNC@20.15.2@MMLCommand@SET PAEMULTQUE
type: MMLCommand
name: SET PAEMULTQUE（设置PAE多队列功能开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PAEMULTQUE
command_category: 配置类
effect_mode: ''
is_dangerous: true
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 配置
status: active
---

# SET PAEMULTQUE（设置PAE多队列功能开关）

## 功能

![](设置PAE多队列功能开关（SET PAEMULTQUE）_11735768.assets/notice_3.0-zh-cn_2.png)

如果修改该配置可能会造成业务流量损失，修改配置后需要复位对应的Pod。

该命令用于设置PAE多队列功能是否使能。

## 注意事项

该命令为高危命令，如果修改该配置可能会造成业务流量损失，修改配置后需要复位对应的Pod。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组。

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENABLE | 功能是否开启 | 可选必选说明：必选参数。<br>参数含义：该参数表示是否使能PAE多队列功能。<br>数据来源：本端规划。<br>取值范围：枚举类型。<br>- disable：去使能。<br>- enable：使能。<br>默认值：enable。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PAEMULTQUE]] · PAE多队列功能开关（PAEMULTQUE）

## 使用实例

开启PAE多队列功能：

```
%%SET PAEMULTQUE: ENABLE=enable;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-PAEMULTQUE.md`
