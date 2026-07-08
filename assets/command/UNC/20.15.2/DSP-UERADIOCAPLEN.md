---
id: UNC@20.15.2@MMLCommand@DSP UERADIOCAPLEN
type: MMLCommand
name: DSP UERADIOCAPLEN（显示UE Radio Capability信元长度）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: UERADIOCAPLEN
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- UE无线能力控制策略
status: active
---

# DSP UERADIOCAPLEN（显示UE Radio Capability信元长度）

## 功能

**适用NF：AMF**

该命令用于显示AMF存储的UE Radio Capability信元长度信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODID | POD ID | 可选必选说明：必选参数<br>参数含义：该参数用于标识系统中的POD ID。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [UE Radio Capability信元长度（UERADIOCAPLEN）](configobject/UNC/20.15.2/UERADIOCAPLEN.md)

## 使用实例

查询PODID为uncpod-0的UE Radio Capability信元长度，执行如下命令：

```
%%DSP UERADIOCAPLEN: PODID="uncpod-0";%%
RETCODE = 0  操作成功

结果如下
--------
                         POD ID  =  uncpod-0
           IMEI设备型号核准号码  =  35437906
UE Radio Capability信元最小长度  =  1024
UE Radio Capability信元最大长度  =  4096
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示UE-Radio-Capability信元长度（DSP-UERADIOCAPLEN）_71436533.md`
