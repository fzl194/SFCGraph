---
id: UNC@20.15.2@MMLCommand@LST BSSAPPTMR
type: MMLCommand
name: LST BSSAPPTMR（查询BSSAPP协议定时器表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: BSSAPPTMR
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- BSSAPP
- BSSAPP参数管理
status: active
---

# LST BSSAPPTMR（查询BSSAPP协议定时器表）

## 功能

**适用网元：SGSN**

此命令用于查询BSSAPP定时器长度配置。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/BSSAPPTMR]] · BSSAPP协议定时器表（BSSAPPTMR）

## 使用实例

查询BSSAPP定时器长度配置：

LST BSSAPPTMR:;

```
%%LST BSSAPPTMR:;%%
RETCODE = 0  操作成功。

查询BSSAPP定时器表
------------------
  等待SPP启动定时器(min)  =  3
    等待VLR可达定时器(s)  =  45
       位置更新定时器(s)  =  15
       GPRS分离定时器(s)  =  4
        GPRS分离重发次数  =  2
   显式IMSI分离定时器(s)  =  4
    显式IMSI分离重发次数  =  2
   隐式IMSI分离定时器(s)  =  4
    隐式IMSI分离重发次数  =  2
   SGSN复位标志定时器(s)  =  8
SGSN复位VLR响应定时器(s)  =  4
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询BSSAPP协议定时器表(LST-BSSAPPTMR)_72225093.md`
