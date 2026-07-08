---
id: UNC@20.15.2@MMLCommand@DSP GRAYUPGRESULT
type: MMLCommand
name: DSP GRAYUPGRESULT（显示灰度升级结果）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: GRAYUPGRESULT
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
- 操作维护
- 灰度升级管理
- 灰度升级前后信息对比管理
status: active
---

# DSP GRAYUPGRESULT（显示灰度升级结果）

## 功能

**适用网元：SGSN、MME**

灰度升级过程分批次执行，该命令用于显示每一个批次升级前后链路资源的比较结果。可通过执行该命令获取到升级前和升级后链路资源的状态变化情况或链路数量变化情况。

## 注意事项

- 仅在升级后网元中可查询到比对结果。
- 灰度升级过程分批次执行，可查看当前批次、历史批次和所有批次的比对结果。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BATCH_IN | 批次 | 可选必选说明：可选参数<br>参数含义：该参数用于指定需要显示的灰度升级的批次。<br>数据来源：本端规划<br>取值范围：<br>- “CURRENT(当前批次)”<br>- “HISTORY(历史批次)”<br>默认值：无。<br>说明：如果参数不填则表示所有批次。 |
| RESTYPE | 资源类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要显示的资源类型。<br>数据来源：本端规划<br>取值范围：<br>- “S1APLINK(S1接口链路)”<br>- “DMLNK(Diameter链路)”<br>- “M3UALINK(M3UA链路)”<br>- “DNSCONN(DNS链路)”<br>- “SGSVLRLNK(SGs链路)”<br>- “LCSAPLNK(LCSAP链路)”<br>- “SBCAPLNK(SBc链路)”<br>- “NSE(NSE标识)”<br>默认值：无。 |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数<br>参数含义：此参数用于指定待查询的服务名称，可以通过<br>[**LST VNFC**](../../../../../../平台服务管理/单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)<br>命令查询得到。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>配置原则：需要填写LINK或GB对应的名称。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@GRAYUPGRESULT]] · 灰度升级结果（GRAYUPGRESULT）

## 使用实例

以下灰度升级分4批次为例，当前正在进行第4批次迁移。

查询当前批次，资源类型为LCSAP链路的升级前后对比结果：

DSP GRAYUPGRESULT: BATCH_IN=CURRENT, RESTYPE=LCSAPLNK, SERVICETYPE="LINK_VNFC";

```
%%DSP GRAYUPGRESULT: BATCH_IN=CURRENT, RESTYPE=LCSAPLNK, 
SERVICETYPE="LINK_VNFC"
;%%
RETCODE = 0  操作成功。

输出结果如下
------------
            批次  =  当前批次
        资源类型  =  LCSAP链路
          资源号  =  4
          链路号  =  4
  升级前链路状态  =  正常
  升级后链路状态  =  正常
升级前后比较结果  =  一致
(结果个数 = 1)
---    END
```

查询历史批次，资源类型为LCSAP链路的升级前后对比结果：

DSP GRAYUPGRESULT: BATCH_IN=HISTORY, RESTYPE=LCSAPLNK, SERVICETYPE="LINK_VNFC";

```
%%DSP GRAYUPGRESULT: BATCH_IN=HISTORY, RESTYPE=LCSAPLNK, 
SERVICETYPE="LINK_VNFC"
;%%
RETCODE = 0  操作成功。

输出结果如下
------------
批次          资源类型     资源号    链路号    升级前链路状态    升级后链路状态    升级前后比较结果

历史批次_3    LCSAP链路    3         3         故障              正常              不一致          
历史批次_2    LCSAP链路    2         2         正常              故障              不一致          
历史批次_1    LCSAP链路    1         1         正常              正常              一致            
(结果个数 = 3)
---    END
```

查询所有批次，资源类型为LCSAP链路的升级前后对比结果：

DSP GRAYUPGRESULT: RESTYPE=LCSAPLNK, SERVICETYPE="LINK_VNFC";

```
%%DSP GRAYUPGRESULT: RESTYPE=LCSAPLNK, 
SERVICETYPE="LINK_VNFC"
;%%
RETCODE = 0  操作成功。

输出结果如下
------------
批次          资源类型     资源号    链路号    升级前链路状态    升级后链路状态    升级前后比较结果

当前批次      LCSAP链路    4         4         正常              正常              一致            
历史批次_3    LCSAP链路    3         3         故障              正常              不一致          
历史批次_2    LCSAP链路    2         2         正常              故障              不一致          
历史批次_1    LCSAP链路    1         1         正常              正常              一致            
(结果个数 = 4)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-GRAYUPGRESULT.md`
