---
id: UDG@20.15.2@MMLCommand@LST PDNAUTOTSTSW
type: MMLCommand
name: LST PDNAUTOTSTSW（查询PDN自动探测开关状态）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: PDNAUTOTSTSW
command_category: 查询类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 会话管理
- 会话连通性检测
- 网络侧连通性检测
- PDN侧路由探测
status: active
---

# LST PDNAUTOTSTSW（查询PDN自动探测开关状态）

## 功能

**适用NF：PGW-U、UPF**

查询PDN自动探测开关状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/PDNAUTOTSTSW]] · PDN自动探测开关状态（PDNAUTOTSTSW）

## 使用实例

查询PDN自动探测开关状态：

```
LST PDNAUTOTSTSW:;
```

```

RETCODE = 0  Operation succeeded

PDN自动探测开关状态
------------------------
PDN Route Auto Test Switch  =  ENABLE
Dns Kpi Fault Test Switch = ENABLE
Path Fault Tracert Test Switch = ENABLE
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-PDNAUTOTSTSW.md`
