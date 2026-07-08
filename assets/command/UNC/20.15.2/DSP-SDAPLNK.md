---
id: UNC@20.15.2@MMLCommand@DSP SDAPLNK
type: MMLCommand
name: DSP SDAPLNK（显示SDUP链路）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SDAPLNK
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- MME链式备份管理
- Sdup接口管理
- Sdup接口调测
status: active
---

# DSP SDAPLNK（显示SDUP链路）

## 功能

**适用网元：MME**

本命令用于查询系统内正在使用的Sdup接口链路详细信息。

输出结果分为两个报表，报表1显示每条链路的状态以及链路指向的对端MME；报表2显示正常与故障状态的链路数量。

## 注意事项

未指定SAP进程号时，显示主控模块所在的SAP进程上的SDUP链路信息。指定SAP进程号时，显示对应进程上的SDUP链路信息。

## 权限

manage-ug；system-ug；monitor-ug；visit-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组；G_4，来宾级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCOPE | 查询范围 | 可选必选说明：可选参数<br>参数含义：本参数用于指示查询Sdup链路信息的范围<br>数据来源：本端规划。<br>取值范围：<br>- “ALL(所有信息)”<br>- “SPECIFIED_MME(指定对端MME)”<br>默认值：<br>“ALL(所有信息)” |
| PEERMMEC | 对端MME编码 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指示目标MME编码。<br>系统按MME编码匹配对应的MME，并获取该MME下的Sdup IP地址，输出结果为包含这些IP地址的Sdup链路信息。<br>前提条件：此参数在<br>“查询范围”<br>参数配置为<br>“SPECIFIED_MME(指定对端MME)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0～255<br>默认值：无 |
| SPECPROC | 指定进程 | 可选必选说明：可选参数<br>参数含义：本参数用于指示是否按指定进程查询Sdup链路信息。<br>数据来源：本端规划<br>取值范围：<br>- “UNSPECIFIED(不指定)”：系统将自动选择支持链路探测的进程查询。<br>- “SPECIFIED(指定)”：系统只向指定的进程查询。<br>默认值：<br>“UNSPECIFIED” |
| RUNAME | RU名称 | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定资源单元名称。<br>前提条件：该参数在<br>“指定进程”<br>参数配置为<br>“SPECIFIED(指定)”<br>后生效。<br>数据来源：该参数可以在MCR_VNFC的CLI中通过DSP RU命令查询。<br>取值范围：1~63位字符串<br>默认值：无 |
| PRON | 进程号 | 可选必选说明：条件必选参数<br>参数含义：本参数用于指示查询的SAP进程号。<br>前提条件：该参数在<br>“指定进程”<br>参数配置为<br>“SPECIFIED(指定)”<br>后生效。<br>数据来源：本端规划<br>取值范围：0～20<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SDAPLNK]] · SDUP链路（SDAPLNK）

## 使用实例

显示Sdup链路信息：

DSP SDAPLNK: SCOPE=ALL, SPECPROC=UNSPECIFIED;

```
%%DSP SDAPLNK: SCOPE=ALL, SPECPROC=UNSPECIFIED;%%
RETCODE = 0  操作成功

操作结果如下：
------------------------
     对端MME编码  =  53
         RU名称   =  MCR_SP_RU_0064
         进程号   =  0
        链路状态  =  正常
      本端IP地址  =  192.168.15.10
      对端IP地址  =  192.168.16.10
仍有后续报告输出
---    END

+++    mcr        2017-02-15 13:55:47
O&M   #HWHandle=172
%%DSP SDAPLNK: SCOPE=ALL, SPECPROC=UNSPECIFIED;%%
RETCODE = 0  操作成功

操作结果如下：
------------------------
正常状态Sdup链路数  =  1
故障状态Sdup链路数  =  0
(结果个数 = 2)
共有2个报表
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示SDUP链路(DSP-SDAPLNK)_72346897.md`
