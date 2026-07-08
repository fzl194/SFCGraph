---
id: UNC@20.15.2@MMLCommand@LST MPSARP
type: MMLCommand
name: LST MPSARP（查询MPS ARP配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MPSARP
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- MPS配置
- MPS ARP信息配置
status: active
---

# LST MPSARP（查询MPS ARP配置）

## 功能

**适用网元：MME**

此命令用于查询MPS功能开关和当前配置的MPS ARP优先级临界值。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [MPS ARP配置（MPSARP）](configobject/UNC/20.15.2/MPSARP.md)

## 使用实例

查询所有MPS ARP配置:

LST MPSARP:;

```
%%LST MPSARP:;%%
RETCODE = 0  操作成功。

输出结果如下
--------------
MPS功能开关  =  关
     优先级  =  8
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询MPS-ARP配置(LST-MPSARP)_72345099.md`
