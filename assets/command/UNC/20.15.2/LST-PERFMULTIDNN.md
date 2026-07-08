---
id: UNC@20.15.2@MMLCommand@LST PERFMULTIDNN
type: MMLCommand
name: LST PERFMULTIDNN（查询MultiDNN性能统计对象）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PERFMULTIDNN
command_category: 查询类
applicable_nf:
- SMF
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# LST PERFMULTIDNN（查询MultiDNN性能统计对象）

## 功能

**适用NF：SMF、PGW-C**

该命令用于查询MultiDNN性能统计对象。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | 数据网络名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示指定的网络切片支持的数据网络名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：无 |
| SST | 切片业务类型 | 可选必选说明：可选参数<br>参数含义：该参数表示切片的业务类型，如eMBB（1）、URLLC（2）、MIoT（3）等协议定义的标准SST，或者运营商自定义的SST。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |
| SD | 切片细分标识 | 可选必选说明：可选参数<br>参数含义：该参数表示根据网络切片所提供的服务特点、所服务的对象差异，对某种网络切片的进一步细分。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是6。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PERFMULTIDNN]] · MultiDNN性能统计对象（PERFMULTIDNN）

## 使用实例

当运营商希望查询一个MultiDNN配置记录，其中DNN为“huawei.com”，SST为1，SD为“010101”作为性能指标对象时，执行如下命令：

```
%%LST PERFMULTIDNN: DNN="huawei.com", SST=1, SD="010101";%%
            RETCODE = 0  操作成功

            结果如下
            --------
            DNN  =  huawei.com
            SST  =  1
            SD  =  010101
            (结果个数 = 1)

            ---    END
        
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PERFMULTIDNN.md`
