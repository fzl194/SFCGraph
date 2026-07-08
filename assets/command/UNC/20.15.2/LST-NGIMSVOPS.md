---
id: UNC@20.15.2@MMLCommand@LST NGIMSVOPS
type: MMLCommand
name: LST NGIMSVOPS（查询VoPS配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGIMSVOPS
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 5G 语音业务管理
- VoPS管理
status: active
---

# LST NGIMSVOPS（查询VoPS配置）

## 功能

**适用NF：AMF**

该命令用于查询AMF侧对PS域IMS语音能力的支持情况。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [VoPS配置（NGIMSVOPS）](configobject/UNC/20.15.2/NGIMSVOPS.md)

## 使用实例

执行如下命令查询AMF侧对PS域IMS语音能力的支持情况，执行如下命令：

```
%%LST NGIMSVOPS:;%%
RETCODE = 0  操作成功

结果如下
--------
          AMF是否支持IMS语音  =  支持
Data Centric类型终端支持VoPS  =  支持
           AMF是否支持IMS语音 =  先查询UE无线能力
   连接态下去激活用户面原因值 =  正常释放
       是否检查用户S1Mode能力 =  关闭
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询VoPS配置（LST-NGIMSVOPS）_09653054.md`
