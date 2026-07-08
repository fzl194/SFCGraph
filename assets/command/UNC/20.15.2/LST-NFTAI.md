---
id: UNC@20.15.2@MMLCommand@LST NFTAI
type: MMLCommand
name: LST NFTAI（查询NF TAI信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NFTAI
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- NF TAI信息管理
status: active
---

# LST NFTAI（查询NF TAI信息）

## 功能

**适用NF：SMF**

该命令用于查询NF实例的TAI信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | NF实例名称 | 可选必选说明：可选参数<br>参数含义：本参数用于指定对应的NF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~50。<br>默认值：无<br>配置原则：<br>本参数需要与ADD NFUUID命令中的NFINSTANCENAME值保持一致。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NFTAI]] · NF TAI信息（NFTAI）

## 使用实例

运营商A需要查询标识为SMF_Instance_0的NF实例支持的TAI。

```
%%LST NFTAI:;%%
RETCODE = 0  操作成功

结果如下
--------
        NF实例名称  =  SMF_Instance_0
      移动国家代码  =  460
          移动网号  =  01
        跟踪区域码  =  000001
  绑定的SMFINFO ID  =  null
绑定的NWDAFINFO ID  =  null
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NFTAI.md`
