---
id: UNC@20.15.2@MMLCommand@DSP SBCAPLNK
type: MMLCommand
name: DSP SBCAPLNK（显示SBc链路状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SBCAPLNK
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
- SBc接口管理
- SBc链路
status: active
---

# DSP SBCAPLNK（显示SBc链路状态）

## 功能

**适用网元：SGSN、MME**

该命令用于查询系统内所有SGP进程上的SBc链路状态。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SBCAPLNK]] · SBc链路（SBCAPLNK）

## 使用实例

DSP SBCAPLNK:;

```
%%DSP SBCAPLNK:;%%
RETCODE = 0  操作成功。

输出结果如下：
-------------------------
     CBC索引  =  0
      进程号  =  6
      RU名称  =  USN_SP_RU_0064
   IP地址类型  =  IPv4
    本地地址1  =  10.2.62.20
    本地地址2  =  255.255.255.255
   本地端口号  =  29168
    对端地址1  =  172.27.168.1
    对端地址2  =  255.255.255.255
   对端端口号  =  29168
      VPN名称  =  _public_
     链路状态  =  正常
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SBCAPLNK.md`
