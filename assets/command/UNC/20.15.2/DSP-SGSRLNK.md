---
id: UNC@20.15.2@MMLCommand@DSP SGSRLNK
type: MMLCommand
name: DSP SGSRLNK（显示SGS服务端链路）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SGSRLNK
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SMSF管理
- SGS服务端链路
status: active
---

# DSP SGSRLNK（显示SGS服务端链路）

## 功能

**适用NF：SMSF**

此命令用于查看SGS服务端链路状态。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRT | 查询方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询SGS服务端链路状态的方式。<br>取值范围：<br>- “ALL(所有)”：查询所有SGS服务端链路的状态。<br>- “LNK(链路)”：通过指定链路索引查询SGS服务端链路的状态。<br>- “LSX(链路集)”：通过指定链路集查询SGS服务端链路的状态。<br>默认值：无 |
| LNK | 链路索引 | 可选必选说明：条件可选参数<br>参数含义：待查询链路的索引。<br>前提条件：该参数在<br>“查询方式”<br>设置为<br>“LNK(链路)”<br>时生效。<br>取值范围：0~6400<br>默认值：无 |
| LSX | 链路集索引 | 可选必选说明：条件可选参数<br>参数含义：待查询链路所属链路集的索引。<br>前提条件：该参数在<br>“查询方式”<br>设置为<br>“LSX(链路集)”<br>时生效。<br>取值范围：0~2000<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SGSRLNK]] · SGS服务端链路（SGSRLNK）

## 使用实例

1. 查询系统内所有的SGS服务端链路状态信息：
  DSP SGSRLNK: SRT=ALL;
  ```
  %%DSP SGSRLNK: SRT=ALL;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
  RU名称           进程号  链路索引  链路集索引  VPN名称  VLR号  链路状态  

  LINK_SP_RU_0064  0       2         1           NULL     1      故障      
  LINK_SP_RU_0064  1       1         1           NULL     1      故障      
  (结果个数 = 2)

  ---    END
  ```
2. 查询指定链路索引的SGS服务端链路状态信息：
  DSP SGSRLNK: SRT=LNK, LNK=1;
  ```
  %%DSP SGSRLNK: SRT=LNK, LNK=1;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
      RU名称  =  LINK_SP_RU_0064
      进程号  =  1
    链路索引  =  1
  链路集索引  =  1
     VPN名称  =  NULL
       VLR号  =  1
    链路状态  =  故障
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SGSRLNK.md`
