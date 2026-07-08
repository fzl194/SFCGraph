---
id: UNC@20.15.2@MMLCommand@LST LCSPARA
type: MMLCommand
name: LST LCSPARA（查询LCS参数表记录）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LCSPARA
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- LCS
- LCS软件参数表
status: active
---

# LST LCSPARA（查询LCS参数表记录）

## 功能

**适用网元：SGSN、MME**

此命令用于查询LCS参数。

## 注意事项

此命令执行后立即生效。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [LCS参数表记录（LCSPARA）](configobject/UNC/20.15.2/LCSPARA.md)

## 使用实例

查询LCS参数设置：

LST LCSPARA:;

```
%%LST LCSPARA:;%%
RETCODE = 0  操作成功。

操作结果如下
--------------
          隐私验证定时器(s)  =  20
    EPC 等待Paging定时器(s)  =  50
      EPC 位置获取定时器(s)  =  20
     EPC Multi IMSI定位方式  =  拒绝
EPC 位置信息表老化时长(min)  =  60
       GU 位置报告定时器(s)  =  30
       GU GMLC响应定时器(s)  =  20
     GU MO继续流程定时器(s)  =  10
   GU GMLC是否限定属于HPLMN  =  不限定属于HPLMN
   EPC UE级的GMLC的鉴权方案  =  仅鉴权同UE相同PLMN的GMLC
             2G LCS定位策略  =  本地定位
             4G LCS定位策略  =  协议模式定位
          启用连接态LRC流程  =  否
       ECM-IDLE态触发Paging  =  是
      延迟定位超时时长(min)  =  720
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询LCS参数表记录(LST-LCSPARA)_26305608.md`
