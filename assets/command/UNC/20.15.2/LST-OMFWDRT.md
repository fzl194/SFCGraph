---
id: UNC@20.15.2@MMLCommand@LST OMFWDRT
type: MMLCommand
name: LST OMFWDRT（查询OM转发路由）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: OMFWDRT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 路由管理
- 代理管理
status: active
---

# LST OMFWDRT（查询OM转发路由）

## 功能

此命令用于查询OM转发路由。

## 注意事项

无。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：可选参数<br>参数含义：网元ID（用来标识网元）<br>取值范围：0~65535<br>默认值：无<br>配置原则：无 |
| SERVICENAME | 服务名称 | 可选必选说明：可选参数<br>参数含义：管道服务名称<br>取值范围：不超过128字符，不包含中文以及如下特殊字符：`~!@#$%^&*()+=\|{}':;,[]<>/?！￥…（）—【】‘；：”“’。，、？<br>默认值：无<br>配置原则：无 |
| PORT | 端口 | 可选必选说明：可选参数<br>参数含义：OMLB外出网络端口<br>取值范围：17100~17199<br>默认值：无<br>配置原则：无 |
| BACKENDPORT | 后端端口 | 可选必选说明：可选参数<br>参数含义：转发目标服务端口<br>取值范围：0~65535<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OMFWDRT]] · OM转发路由（OMFWDRT）

## 使用实例

查询OM转发路由信息：

```
%%LST OMFWDRT:;%%
RETCODE = 0  操作成功

操作结果如下
------------
网元ID 服务名称 端口   后端端口

0      OMG      17100  22
0      OMG      17101  22
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-OMFWDRT.md`
