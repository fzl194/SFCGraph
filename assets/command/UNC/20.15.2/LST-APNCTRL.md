---
id: UNC@20.15.2@MMLCommand@LST APNCTRL
type: MMLCommand
name: LST APNCTRL（查询APN控制参数配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: APNCTRL
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
- 移动性管理
- 基于APN的MM拥塞控制_流控_寻呼优化配置
status: active
---

# LST APNCTRL（查询APN控制参数配置）

## 功能

**适用网元：SGSN、MME**

该命令用于查询一条或多条APN信令拥塞控制和固定终端寻呼优化的APN控制参数配置。

## 注意事项

该命令中如果输入了 “SUBSCRIBEDAPN(签约APN)” ，则查询指定APN对应的配置；如果没有输入 “SUBSCRIBEDAPN(签约APN)” ，则查询所有的APN控制参数配置。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBSCRIBEDAPN | 签约APN | 可选必选说明：可选参数<br>参数含义：该参数用于指定<br>“签约APN”<br>。<br>取值范围：1~62位字符串<br>默认值：无<br>说明：“签约APN”<br>（APN网络标识地址）由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/APNCTRL]] · APN控制参数配置（APNCTRL）

## 使用实例

1.查询一条 “签约APN” 为 “huawei.com” 的APN控制参数配置：

LST APNCTRL: SUBSCRIBEDAPN="huawei.com";

```
%%LST APNCTRL: SUBSCRIBEDAPN="huawei.com";%%
RETCODE = 0  操作成功。

操作结果如下
------------
                          签约APN  =  HUAWEI.COM
                          APN类型  =  拥塞控制APN
                        APN优先级  =  低
            Backoff Timer分配开关  =  关
       Back off timer最小值（秒）  =  660
       Back off timer最大值（秒）  =  3000
                   附着拒绝原因值  =  拥塞
识别异常附着行为的门限（次/小时）  =  30
      Ready Timer定时器时长（秒）  =  NULL
            T3324定时器时长（秒）  =  NULL
            T3312定时器时长（分）  =  NULL
(结果个数 = 1)
---    END
```

2.查询全部的APN控制配置：

LST APNCTRL:;

```
%%LST APNCTRL:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
签约APN        APN类型        APN优先级    Backoff Timer分配开关    Back off timer最小值（秒）    Back off timer最大值（秒）    附着拒绝原因值    识别异常附着行为的门限（次/小时）    Ready Timer定时器时长（秒）    T3324定时器时长（秒）    T3312定时器时长（分）

HUAWEI.COM     拥塞控制APN    低           关                       660                           3000                          拥塞              30                                   NULL                           NULL                     NULL                 
HUAWEI1.COM    Both           低           开                       660                           3000                          拥塞              30                                   180                            180                      54                   
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-APNCTRL.md`
