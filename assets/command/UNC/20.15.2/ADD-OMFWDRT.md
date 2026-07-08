---
id: UNC@20.15.2@MMLCommand@ADD OMFWDRT
type: MMLCommand
name: ADD OMFWDRT（增加OM转发路由）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: OMFWDRT
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 路由管理
- 代理管理
status: active
---

# ADD OMFWDRT（增加OM转发路由）

## 功能

此命令用于增加外部访问内部指定服务的OM转发路由。

## 注意事项

该命令仅限角色为Administrators的用户执行。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：必选参数<br>参数含义：网元ID（用来标识网元）<br>取值范围：0~65535<br>默认值：无<br>配置原则：无 |
| SERVICENAME | 服务名称 | 可选必选说明：必选参数<br>参数含义：管道服务名称<br>取值范围：OMG<br>默认值：OMG<br>配置原则：无 |
| PORT | 端口 | 可选必选说明：必选参数<br>参数含义：OMLB外出网络端口<br>取值范围：17100~17199<br>默认值：无<br>配置原则：无 |
| BACKENDPORT | 后端端口 | 可选必选说明：必选参数<br>参数含义：转发目标服务端口<br>取值范围：22，2022<br>默认值：2022<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OMFWDRT]] · OM转发路由（OMFWDRT）

## 使用实例

增加新的OM转发路由：

```
%%ADD OMFWDRT: MEID=0, SERVICENAME="OMG", PORT=17100, BACKENDPORT=22;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-OMFWDRT.md`
