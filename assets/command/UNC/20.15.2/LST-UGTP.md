---
id: UNC@20.15.2@MMLCommand@LST UGTP
type: MMLCommand
name: LST UGTP（查询GTP-C路径扫描参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UGTP
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
- GTP-C接口管理
- GTP-C协议管理
- GTP-C路径扫描参数
status: active
---

# LST UGTP（查询GTP-C路径扫描参数）

## 功能

**适用网元：SGSN、MME**

该命令用于查询GTP信息表。该信息表包含了SPP和UPP进程的运行控制参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [GTP-C路径扫描参数（UGTP）](configobject/UNC/20.15.2/UGTP.md)

## 使用实例

查询GTP信息表：

LST UGTP:;

```
%%LST UGTP:;%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
    空闲计数器扫描间隔(秒)  =  180
      SM信令路径空闲计数器  =  60
      MM信令路径空闲计数器  =  60
      GTPMAP路径空闲计数器  =  60
路径版本探测扫描周期(分钟)  =  60
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询GTP-C路径扫描参数(LST-UGTP)_72225595.md`
