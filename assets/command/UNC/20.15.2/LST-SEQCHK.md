---
id: UNC@20.15.2@MMLCommand@LST SEQCHK
type: MMLCommand
name: LST SEQCHK（查询序号检查信息表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SEQCHK
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
- GnGp接口管理
- GTP用户面管理
- 序号检查信息管理
status: active
---

# LST SEQCHK（查询序号检查信息表）

## 功能

**适用网元：SGSN、MME**

此命令用于查询GTP序号检查开关的状态。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SEQCHK]] · 序号检查信息表（SEQCHK）

## 使用实例

查询GTP的序号检查开关：

LST SEQCHK:;

```
%%LST SEQCHK:;%%
RETCODE = 0  执行成功。

输出结果如下
------------------
 序号检查功能开关  =  关
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SEQCHK.md`
