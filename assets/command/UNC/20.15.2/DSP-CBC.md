---
id: UNC@20.15.2@MMLCommand@DSP CBC
type: MMLCommand
name: DSP CBC（显示CBC链路状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CBC
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- SBc接口管理
- CBC配置
status: active
---

# DSP CBC（显示CBC链路状态）

## 功能

**适用网元：SGSN、MME**

此命令用于查询CBC下SBc链路的连接状态。

## 注意事项

- 该命令执行后立即生效。
- 如果不输入CBC索引号，则显示所有CBC下SBc链路的连接状态。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CBCIDX | CBC索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定待查询的CBC索引。<br>数据来源：本端规划<br>取值范围：0~127<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CBC]] · CBC（CBC）

## 使用实例

输入CBC索引，查询指定的CBC数据：

DSP CBC: CBCIDX=0;

```
%%DSP CBC: CBCIDX=0;%%
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

- 原始手册：`evidence/UNC/20.15.2/DSP-CBC.md`
