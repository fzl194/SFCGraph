---
id: UNC@20.15.2@MMLCommand@DSP SGSLNK
type: MMLCommand
name: DSP SGSLNK（显示SGs链路状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SGSLNK
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 电路域联合业务
- SGSAP
- SGsAP链路管理
status: active
---

# DSP SGSLNK（显示SGs链路状态）

## 功能

**适用网元：MME**

此命令用于查看SGs链路状态。

## 注意事项

无

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRT | 查询方式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询SGs链路状态的方式。<br>取值范围：<br>- “ALL(所有)”：查询所有SGs链路的状态。<br>- “LNK(链路)”：通过指定链路索引查询SGs链路的状态。<br>- “LSX(链路集)”：通过指定链路集查询SGs链路的状态。<br>- “VLR(VLR号)”：通过指定VLR号查询SGs链路的状态。<br>默认值：无 |
| LNK | 链路索引 | 可选必选说明：条件可选参数<br>参数含义：待查询链路的索引。<br>前提条件：该参数在<br>“查询方式”<br>设置为<br>“LNK(链路)”<br>时生效。<br>取值范围：0~511<br>默认值：无 |
| LSX | 链路集索引 | 可选必选说明：条件可选参数<br>参数含义：待查询链路所属链路集的索引。<br>前提条件：该参数在<br>“查询方式”<br>设置为<br>“LSX(链路集)”<br>时生效。<br>取值范围：0~255<br>默认值：无 |
| VN | VLR号 | 可选必选说明：条件可选参数<br>参数含义：待查询链路的VLR号。<br>前提条件：该参数在<br>“查询方式”<br>设置为<br>“VLR(VLR号)”<br>时生效。<br>取值范围：1~15位十进制数字<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SGSLNK]] · SGs链路（SGSLNK）

## 使用实例

1. 查询系统内所有的SGs链路状态信息：
  DSP SGSLNK: SRT=ALL;
  ```
  %%DSP SGSLNK: SRT=ALL;%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
  RU 名称           进程号    	 链路索引     链路集索引       VPN名称     VLR号         SGs链路状态

  USN_SP_RU_0064    1              7             7                NULL        86139064210    故障           
  USN_SP_RU_0065    0              6             6                NULL        86139064209    故障           
  USN_SP_RU_0064    0              5             5                NULL        86139064208    故障           
  USN_SP_RU_0065    1              4             4                NULL        86139064207    故障           
  USN_SP_RU_0064    1              3             3                NULL        86139064206    故障           
  USN_SP_RU_0065    0              2             2                NULL        86139064205    故障           
  USN_SP_RU_0064    0              1             1                NULL        86139064204    故障           
  USN_SP_RU_0065    1              0             0                NULL        86139064203    故障           
  USN_SP_RU_0064    1              8             8                NULL        1230301        故障           
  (结果个数 = 9)

  ---    END
  ```
2. 查询指定VLR号的SGs链路状态信息：
  DSP SGSLNK: SRT=VLR, VN="1230301";
  ```
  %%DSP SGSLNK: SRT=VLR, VN="1230301";%%
  RETCODE = 0  操作成功。

  操作结果如下
  --------------
          RU名称  =  USN_SP_RU_0064
          进程号  =  1
        链路索引  =  8
      链路集索引  =  8
         VPN名称  =  NULL
           VLR号  =  1230301
      SGs链路状态  =  故障
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SGSLNK.md`
