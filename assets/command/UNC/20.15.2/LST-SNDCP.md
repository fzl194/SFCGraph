---
id: UNC@20.15.2@MMLCommand@LST SNDCP
type: MMLCommand
name: LST SNDCP（查询SNDCP参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SNDCP
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- SNDCP参数
status: active
---

# LST SNDCP（查询SNDCP参数）

## 功能

**适用网元：SGSN**

该命令用来查询SNDCP层系统参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/SNDCP]] · SNDCP参数状态（SNDCP）

## 使用实例

查询SNDCP参数:

LST SNDCP:;

```
%%LST SNDCP:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
            最大缓冲N-PDU数  =  20000
   每个NSAPI最大缓冲N-PDU数  =  5
             负流量阈值(KB)  =  10
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SNDCP参数(LST-SNDCP)_72225705.md`
