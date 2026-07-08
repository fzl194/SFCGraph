---
id: UNC@20.15.2@MMLCommand@LST SCCPTMR
type: MMLCommand
name: LST SCCPTMR（查询SCCP定时器参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCCPTMR
command_category: 查询类
applicable_nf:
- SGSN
- MME
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCCP管理
- SCCP定时器
status: active
---

# LST SCCPTMR（查询SCCP定时器参数）

## 功能

**适用网元：SGSN、MME、SMSF**

此命令用来查询SCCP定时器参数记录。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SCCPTMR]] · SCCP定时器参数（SCCPTMR）

## 使用实例

查询SCCP定时器的所有记录：

LST SCCPTMR:;

```
%%LST SCCPTMR:;%%
RETCODE = 0  操作成功。

SCCP协议定时器
--------------
       连接建立定时器(s)  =  90
   不活动性发送定时器(s)  =  450
   不活动性接收定时器(s)  =  1000
       连接释放定时器(s)  =  15
   连接重复释放定时器(s)  =  15
   连接释放外围定时器(s)  =  60
           保护定时器(s)  =  1440
           复位定时器(s)  =  15
           重装定时器(s)  =  15
     子系统测试定时器(s)  =  60
           协调定时器(s)  =  90
 忽略子系统测试定时器(s)  =  60
       资源冻结定时器(s)  =  30
             EA定时器(s)  =  10
        LRN冻结定时器(s)  =  15
       资源核查定时器(s)  =  3600
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SCCPTMR.md`
