---
id: UNC@20.15.2@MMLCommand@DSP SBCMME
type: MMLCommand
name: DSP SBCMME（显示SBC MME链路状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SBCMME
command_category: 查询类
applicable_nf:
- CBCF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- SBc接口管理
- SBC MME配置
status: active
---

# DSP SBCMME（显示SBC MME链路状态）

## 功能

**适用网元：CBCF**

此命令用于查询SBC MME下SBc链路的连接状态。

## 注意事项

- 该命令执行后立即生效。
- 如果不输入MME索引号，则显示所有SBC MME下SBc链路的连接状态。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEIDX | MME索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询的MME索引。<br>数据来源：本端规划<br>取值范围：0~127<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SBCMME]] · SBC MME实体（SBCMME）

## 使用实例

输入MME索引，查询指定的SBC MME数据：

```
%%DSP SBCMME: MMEIDX=0;%%
RETCODE = 0  操作成功。

输出结果如下：
-------------------------
     MME 索引  =  0
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

- 原始手册：`evidence/UNC/20.15.2/DSP-SBCMME.md`
