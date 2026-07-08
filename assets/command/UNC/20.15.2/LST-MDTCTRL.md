---
id: UNC@20.15.2@MMLCommand@LST MDTCTRL
type: MMLCommand
name: LST MDTCTRL（查询MDT控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MDTCTRL
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- MDT管理
status: active
---

# LST MDTCTRL（查询MDT控制参数）

## 功能

**适用网元：MME**

该命令用于查询MDT控制参数。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@MDTCTRL]] · MDT控制参数（MDTCTRL）

## 使用实例

查询MDT控制参数：

LST MDTCTRL:;

```
%%LST MDTCTRL:;%%
RETCODE = 0  操作成功

操作结果如下
--------------
                           MDT开关  =  ON
是否向新侧MME携带MDT-Configuration  =  ON
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-MDTCTRL.md`
