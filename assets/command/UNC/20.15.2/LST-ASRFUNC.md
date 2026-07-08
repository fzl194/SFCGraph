---
id: UNC@20.15.2@MMLCommand@LST ASRFUNC
type: MMLCommand
name: LST ASRFUNC（查询容灾功能参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ASRFUNC
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 主备容灾管理
- 容灾功能参数
status: active
---

# LST ASRFUNC（查询容灾功能参数）

## 功能

**适用网元：SGSN、MME**

该命令用于查询容灾功能参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/ASRFUNC]] · 容灾功能参数（ASRFUNC）

## 使用实例

查询容灾功能参数：

LST ASRFUNC:;

```
%%LST ASRFUNC:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
容灾功能参数  =  开启
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ASRFUNC.md`
