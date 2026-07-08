---
id: UNC@20.15.2@MMLCommand@DSP CLRDNSCPROG
type: MMLCommand
name: DSP CLRDNSCPROG（查询离散清缓存进度）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CLRDNSCPROG
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
- 系统管理
- DNS维护管理
- 清除DNS Cache
status: active
---

# DSP CLRDNSCPROG（查询离散清缓存进度）

## 功能

**适用网元：SGSN、MME**

该命令用于查询一级Cache离散清除进度。

DNS Cache是使用DNS服务器解析时查找到的域名和IP地址信息在系统中的缓存，用于快速解析域名。

DNS Cache分为一级Cache和二级Cache。一级Cache保存在SPP进程上，保存了每个SPP进程各自常用的域名记录；二级Cache保存在1号SGP进程上，保存的域名记录为每个SPP进程中域名记录的集合。当SPP进程需要获取域名记录时，首先在HOSTFILE中查询。如果HOSTFILE中查询不到需要的域名记录，则在一级Cache中进行查询。如果一级Cache中查询不到需要的域名记录，则在二级Cache上查询。如果二级Cache仍查询不到需要的域名记录，则向DNS服务器进行查询。

每条Cache的记录具有一定的生命周期，生命周期结束后，该记录失效。

DNS服务器上的数据修改后，可以使用CLR DNSC命令清除MME网元整系统DNS Cache，即使用命令清除二级Cache和一级Cache。

当软参BYTE_EX_B25 BIT1、BYTE_EX_B25 BIT3~BIT4、BYTE_EX_B322 BIT1~BIT2或者BYTE_EX_B332 BIT6不为0时，打开离散清缓存功能，即执行CLR DNSC并不会立即清除一级Cache，按照软参说明离散清除一级Cache。DSP CLRDNSCPROG命令用于在BYTE_EX_B25 BIT1、BYTE_EX_B25 BIT3~BIT4、BYTE_EX_B322 BIT1~BIT2或者BYTE_EX_B332 BIT6不为0时，查询一级Cache离散清除进度。

## 注意事项

- 该命令执行后立即生效。
- OMU虚机复位后一级Cache离散清除进度会清空。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数<br>参数含义：此参数用于指定待查询的服务名称，可以通过<br>[**LST VNFC**](../../../../../../平台服务管理/单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)<br>命令查询得到。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>配置原则：<br>当前参数填写请与之前执行的CLR DNSC清缓存命令输入的服务名称参数保持一致。<br>- 如果执行CLR DNSC清缓存时“Cache类型”参数配置为“L1CACHE(一级Cache)”，则SERVICETYPE需要填写USN_VNFC的名称。<br>- 如果执行CLR DNSC清缓存时“Cache类型”参数配置为“L2CACHE(二级Cache)”，则SERVICETYPE需要填写LINK_VNFC的名称。<br>- 如果执行CLR DNSC清缓存时“Cache类型”参数配置为“ALL(所有Cache)”，则SERVICETYPE需要填写LINK_VNFC的名称。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CLRDNSCPROG]] · 离散清缓存进度（CLRDNSCPROG）

## 使用实例

DSP CLRDNSCPROG: SERVICETYPE="LINK_VNFC";

```
%%DSP CLRDNSCPROG: SERVICETYPE="LINK_VNFC";%% 
RETCODE = 0  操作成功  

查询结果如下 
------------           
          离散清缓存状态  =  可以执行离散清缓存       
      离散清缓存开始时间  =  NULL 
需要离散清缓存总进程个数  =  0 
已完成离散清缓存进程个数  =  0     
    离散清缓存进度百分比  =  0      
      离散清缓存剩余时间  =  0                 
                服务名称  =  LINK_VNFC 
(结果个数 = 1) 

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-CLRDNSCPROG.md`
