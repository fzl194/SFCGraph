---
id: UNC@20.15.2@MMLCommand@LST GBPAGING
type: MMLCommand
name: LST GBPAGING（查询Gb接口寻呼数据）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GBPAGING
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- Gb接口寻呼数据
status: active
---

# LST GBPAGING（查询Gb接口寻呼数据）

## 功能

**适用网元：SGSN**

该命令用于查看2G寻呼配置参数。2G寻呼表是系统根据小区配置自动维护的，在判断路由更新类型，发送寻呼命令时，需要使用此命令。

## 注意事项

- 不输入参数，表示查询所有参数。
- 输入参数“LAI”时，查询所有属于该LAI的参数。
- 输入参数“LAI”＋“RAC”，则查询由LAI和RAC确定的参数。
- 输入参数“NSEI”时，查询该NSE下的所有寻呼配置参数。
- 输入“LAI”+“RAC”+“NSEI”，查询该条件唯一确定的参数。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICETYPE | 服务名称 | 可选必选说明：必选参数<br>参数含义：此参数用于指定待查询的服务名称，可以通过<br>[**LST VNFC**](../../../../../平台服务管理/单体服务平台功能管理/操作维护/配置管理/VNFC信息/查询VNFC（LST VNFC）_59036046.md)<br>命令查询得到。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。<br>默认值：无<br>配置原则：需要填写GB或USN对应的名称。 |
| LAI | 寻呼范围位置区标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由区所在的位置区标识，与RAC共同构成路由区标识。LAI = MNC + MCC + LAC。<br>数据来源：整网规划<br>取值范围：9~10位十六进制数<br>默认值：无 |
| RAC | 寻呼范围路由区编码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由区在位置区内的标识，与LAI共同构成路由区标识。<br>数据来源：整网规划<br>取值范围：1~4位十六进制数<br>默认值：无 |
| NSEI | NSE标识 | 可选必选说明：可选参数<br>参数含义：该参数用于指定路由区所在信令实体标识。该参数确定该路由区在哪一个NSE实体上。<br>数据来源：整网规划<br>取值范围：0~65535<br>默认值：无 |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：0~63位字符串<br>默认值：无 |

## 操作的配置对象

- [Gb接口寻呼数据（GBPAGING）](configobject/UNC/20.15.2/GBPAGING.md)

## 使用实例

查询Gb接口所有寻呼数据：

LST GBPAGING: SERVICETYPE="USN_VNFC" ;

```
%%LST GBPAGING: 
SERVICETYPE="USN_VNFC"
;%%
RETCODE = 0  操作成功。

操作结果如下
-------------------------
寻呼范围位置区标识    寻呼范围路由区编码    NSE标识     RU名称          进程号

 123033811              0x08                13801      GB_SP_RU_0064     1          
 123033801              0x02                13801      GB_SP_RU_0064     1          
 123033801              0x01                13801      GB_SP_RU_0064     1          
(结果个数 = 3) 
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询Gb接口寻呼数据(LST-GBPAGING)_26146008.md`
