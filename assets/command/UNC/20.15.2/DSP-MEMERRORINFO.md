---
id: UNC@20.15.2@MMLCommand@DSP MEMERRORINFO
type: MMLCommand
name: DSP MEMERRORINFO（显示内存错误信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MEMERRORINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 资源管理
- RU管理
status: active
---

# DSP MEMERRORINFO（显示内存错误信息）

## 功能

该命令用于查询内存错误信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数表示RU名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：当不输入时显示所有资源的信息。 |
| VERBOSE | 详细信息 | 可选必选说明：可选参数<br>参数含义：该参数用于表示是否显示详细信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NO：否。<br>- YES：是。<br>默认值：NO |
| SHOWNUMBER | 要查询的数据最大个数 | 可选必选说明：可选参数<br>参数含义：该参数用于表示每个RU能够显示的最大记录量。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～10。<br>默认值：1<br>配置原则：当不输入时，若是某个资源的实际数据量达到此参数的默认值，则显示的数据量为此参数默认值，否则按实际数据量显示。当输入某个值时，若是某个资源的实际数据量达到此参数值，则显示的数据量为此参数值，否则按实际数据量显示。 |
| BEGININDEX | 记录起始位置 | 可选必选说明：可选参数<br>参数含义：该参数用于表示每个RU从第几条记录开始显示。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～9。<br>默认值：无<br>配置原则：当不输入时，从最新的数据开始显示，否则从指定的起始数据索引开始显示。 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识，但不能填写0，0表示VNFP。 |

## 操作的配置对象

- [内存错误信息（MEMERRORINFO）](configobject/UNC/20.15.2/MEMERRORINFO.md)

## 使用实例

查询内存错误信息：

```
DSP MEMERRORINFO:BEGININDEX=0
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
                RU编号  =  1
                进程ID  =  1006
              进程名称  =  APPLocation10001
          内存故障类型  =  Memory Damage
          内存释放地址  =  140708660913712
  内存释放发生的文件名  =  test_log.log
内存释放发生的文件行号  =  10
              发生时间  =  2017-02-10 11:33:14
    上次申请内存的文件  =  NULL
上次申请内存的文件行号  =  0
  上次申请内存时的Tick  =  0
    上次释放内存的文件  =  NULL
上次释放内存的文件行号  =  0
           DOPRA版本号  =  DOPRA SSP V300R002C70SPC011
           FENIX版本号  =  FENIXV100R005C00B162
            补丁版本号  =  NULL
                调用栈  =  NULL
                转储栈  =  NULL     
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示内存错误信息（DSP-MEMERRORINFO）_59103543.md`
