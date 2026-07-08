---
id: UNC@20.15.2@MMLCommand@LST NRFCONNPLCY
type: MMLCommand
name: LST NRFCONNPLCY（查询NRF国际漫游连接策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NRFCONNPLCY
command_category: 查询类
applicable_nf:
- NRF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF国际漫游参数管理
status: active
---

# LST NRFCONNPLCY（查询NRF国际漫游连接策略）

## 功能

**适用NF：NRF**

此命令用于查询NRF对接NF/NRF时的国际漫游的连接策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERNFTYPE | 对端NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于表示对端NF类型。<br>数据来源：本端规划<br>取值范围：<br>- NRF（NRF）<br>- NF（NF）<br>默认值：无<br>配置原则：无 |
| CONNPOLICY | 国际漫游连接策略 | 可选必选说明：可选参数<br>参数含义：该参数用于表示国际漫游连接策略。<br>数据来源：全网规划<br>取值范围：<br>- “DIRECT（DIRECT）”：与对端NF直接通信，不通过SEPP。<br>- “SBI_TARGET_APIROOT（SBI_TARGET_APIROOT）”：与对端NF通过SEPP交互，在http头中携带对端NF的地址信息。<br>- “HTTP_PROXY（HTTP_PROXY）”：与对端NF通过SEPP交互，在URI中携带对端NF的地址信息。<br>默认值：无<br>配置原则：<br>建议本PLMN内NF与SEPP的连接和NRF与SEPP的连接策略保持一致。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFCONNPLCY]] · NRF国际漫游连接策略（NRFCONNPLCY）

## 使用实例

使用以下命令查询NRF对接NF/NRF时的国际漫游的连接策略。

```
LST NRFCONNPLCY
%%LST NRFCONNPLCY:;%%
RETCODE = 0  操作成功

结果如下
--------
      对端NF类型  =  NRF
国际漫游连接策略  =  DIRECT
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NRFCONNPLCY.md`
