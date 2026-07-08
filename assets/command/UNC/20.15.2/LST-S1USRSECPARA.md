---
id: UNC@20.15.2@MMLCommand@LST S1USRSECPARA
type: MMLCommand
name: LST S1USRSECPARA（查询S1模式用户安全配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: S1USRSECPARA
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 用户安全管理
- S1模式用户安全参数
status: active
---

# LST S1USRSECPARA（查询S1模式用户安全配置）

## 功能

**适用网元：MME**

此命令用于查询指定号段的用户的鉴权、加密、完整性保护等安全配置

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIPRE | IMSI前缀 | 可选必选说明：可选参数<br>参数含义：待查询的IMSI前缀。<br>取值范围：5~15位数字<br>默认值：无<br>说明：- 在查询特定用户群的安全配置时需要输入IMSI前缀。<br>- 在查询所有安全配置的场景时不填写该字段，结果包括全系统默认配置和特定用户配置。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@S1USRSECPARA]] · S1模式用户安全配置（S1USRSECPARA）

## 使用实例

1. 查询用户群的安全配置：
  LST S1USRSECPARA: IMSIPRE="30802";
  ```
  %%LST S1USRSECPARA: IMSIPRE="30802";%%
  RETCODE = 0  操作成功。

  特殊配置信息查询结果如下
  ------------------------
        IMSI前缀  =  30802
        安全策略  =  只鉴权
      完整性算法  =  NULL
        加密算法  =  NULL
        鉴权事件  =  附着 & INTER TAU & 系统间切换类型的INTRA TAU
        鉴权周期  =  24
    鉴权事件上限  =  1023
      鉴权集数量  =  1
  是否预取鉴权集  =  否
  (结果个数 = 1)
  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-S1USRSECPARA.md`
